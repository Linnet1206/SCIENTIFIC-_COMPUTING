import numpy as np
from scipy.optimize import root


def intersection_residuals(point):
    x_value, y_value = point
    return np.array([x_value**2 + y_value**2 - 4.0, y_value - (x_value**2 - 1.0)])


def main():
    for guess in ([1.0, 1.0], [-1.0, 1.0]):
        solution = root(intersection_residuals, guess)
        residual = intersection_residuals(solution.x)
        print(f"Initial guess {guess}: intersection={solution.x}")
        print(
            f"Converged: {solution.success}; residual norm={np.linalg.norm(residual):.2e}"
        )

    changed_guess = root(intersection_residuals, [1.5, 1.0])
    print("\nChanged initial guess to [1.5, 1.0]")
    print("Intersection:", changed_guess.x)


if __name__ == "__main__":
    main()
