from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def jacobi(coefficients, values, tolerance=1e-8, max_iterations=500):
    diagonal = np.diag(coefficients)
    remainder = coefficients - np.diagflat(diagonal)
    estimate = np.zeros_like(values)
    errors = []
    for _ in range(max_iterations):
        updated = (values - remainder @ estimate) / diagonal
        errors.append(np.linalg.norm(updated - estimate, ord=np.inf))
        estimate = updated
        if errors[-1] < tolerance:
            return estimate, errors
    raise RuntimeError("Jacobi iteration did not converge")


def gauss_seidel(coefficients, values, tolerance=1e-8, max_iterations=500):
    estimate = np.zeros_like(values)
    errors = []
    for _ in range(max_iterations):
        previous = estimate.copy()
        for row in range(len(values)):
            left = coefficients[row, :row] @ estimate[:row]
            right = coefficients[row, row + 1 :] @ previous[row + 1 :]
            estimate[row] = (values[row] - left - right) / coefficients[row, row]
        errors.append(np.linalg.norm(estimate - previous, ord=np.inf))
        if errors[-1] < tolerance:
            return estimate, errors
    raise RuntimeError("Gauss-Seidel iteration did not converge")


def main():
    coefficients = np.array(
        [
            [2.0, -1.0, 0.0, 0.0, 0.0],
            [-1.0, 2.0, -1.0, 0.0, 0.0],
            [0.0, -1.0, 2.0, -1.0, 0.0],
            [0.0, 0.0, -1.0, 2.0, -1.0],
            [0.0, 0.0, 0.0, -1.0, 2.0],
        ]
    )
    values = np.array([100.0, 0.0, 0.0, 0.0, 20.0])
    jacobi_solution, jacobi_errors = jacobi(coefficients, values)
    gs_solution, gs_errors = gauss_seidel(coefficients, values)
    exact_solution = np.linalg.solve(coefficients, values)

    print("Jacobi temperatures:", jacobi_solution)
    print("Gauss-Seidel temperatures:", gs_solution)
    print("Direct solution:", exact_solution)
    print(f"Iterations: Jacobi={len(jacobi_errors)}, Gauss-Seidel={len(gs_errors)}")

    _, relaxed_errors = jacobi(coefficients, values, tolerance=1e-4)
    print(f"Changed tolerance to 1e-4: Jacobi iterations={len(relaxed_errors)}")

    output_dir = Path(__file__).resolve().parents[1] / "outputs"
    output_dir.mkdir(exist_ok=True)
    plt.semilogy(jacobi_errors, label="Jacobi")
    plt.semilogy(gs_errors, label="Gauss-Seidel")
    plt.xlabel("Iteration")
    plt.ylabel("Maximum change")
    plt.title("Convergence of iterative temperature solution")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "task_08_convergence.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Plot saved to outputs/task_08_convergence.png")


if __name__ == "__main__":
    main()
