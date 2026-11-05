import numpy as np
from scipy.linalg import lu_factor, lu_solve


def main():
    coefficients = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 3.0]])
    measurements = [
        np.array([15.0, 10.0, 10.0]),
        np.array([16.0, 11.0, 9.0]),
        np.array([14.0, 12.0, 11.0]),
    ]
    factorization = lu_factor(coefficients)

    for index, values in enumerate(measurements, start=1):
        solution = lu_solve(factorization, values)
        residual_norm = np.linalg.norm(values - coefficients @ solution)
        print(
            f"Measurement set {index}: solution={solution}, residual norm={residual_norm:.2e}"
        )

    changed_values = np.array([18.0, 10.0, 10.0])
    changed_solution = lu_solve(factorization, changed_values)
    print("\nChanged first measurement from 15 to 18")
    print("Reused LU solution:", changed_solution)
    print(
        "Direct-solve agreement:",
        np.allclose(changed_solution, np.linalg.solve(coefficients, changed_values)),
    )


if __name__ == "__main__":
    main()
