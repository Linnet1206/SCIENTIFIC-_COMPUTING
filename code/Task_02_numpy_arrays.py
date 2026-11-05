import numpy as np


def main():
    temperatures_c = np.array(
        [
            18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
            21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
            29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
            23.4, 22.1, 21.0, 20.2, 19.6, 19.0,
        ],
        dtype=float,
    )
    warmer_day_c = temperatures_c + 2.0

    print("Baseline day (24 hourly readings)")
    print(f"Mean: {np.mean(temperatures_c):.2f} C")
    print(f"Minimum: {np.min(temperatures_c):.2f} C")
    print(f"Maximum: {np.max(temperatures_c):.2f} C")
    print("First six readings in Fahrenheit:", (1.8 * temperatures_c + 32)[:6])
    print("\nParameter change: add 2.0 C to every reading")
    print(f"Changed mean: {np.mean(warmer_day_c):.2f} C")
    print(f"Changed minimum: {np.min(warmer_day_c):.2f} C")
    print(f"Changed maximum: {np.max(warmer_day_c):.2f} C")


if __name__ == "__main__":
    main()