import numpy as np


def solve_server_counts(cpu_total):
    coefficients = np.array([[4.0, 2.0], [8.0, 12.0]])
    totals = np.array([cpu_total, 72.0])
    solution = np.linalg.solve(coefficients, totals)
    return coefficients, totals, solution


def main():
    coefficients, totals, solution = solve_server_counts(20.0)
    print(f"Baseline Type A servers: {solution[0]:.0f}")
    print(f"Baseline Type B servers: {solution[1]:.0f}")
    print("Reconstructed resource totals:", coefficients @ solution)
    print("Residual:", totals - coefficients @ solution)

    _, _, changed = solve_server_counts(24.0)
    print("\nChanged CPU total from 20 to 24 units")
    print(f"Type A servers: {changed[0]:.0f}")
    print(f"Type B servers: {changed[1]:.0f}")


if __name__ == "__main__":
    main()
