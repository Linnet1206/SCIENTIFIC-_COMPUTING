import numpy as np


def main():
    calculated = 0.1 + 0.2
    expected = 0.3
    true_value = np.sqrt(2.0)
    approximation = 1.414

    print(f"0.1 + 0.2 = {calculated:.17f}")
    print("Exact comparison:", calculated == expected)
    print("Tolerance-based comparison:", np.isclose(calculated, expected))
    print(f"Absolute approximation error: {abs(true_value - approximation):.8f}")
    print(
        f"Relative approximation error: {abs(true_value - approximation) / abs(true_value):.8%}"
    )

    print("\nCancellation-prone versus stable evaluation")
    for value in (1e-4, 1e-8, 1e-12):
        direct = (np.sqrt(1.0 + value) - 1.0) / value
        stable = 1.0 / (np.sqrt(1.0 + value) + 1.0)
        print(f"x={value:.0e}: direct={direct:.12f}, stable={stable:.12f}")

    changed_value = 1e-6
    print(
        f"\nChanged input x={changed_value:.0e}: stable estimate={1 / (np.sqrt(1 + changed_value) + 1):.12f}"
    )


if __name__ == "__main__":
    main()
