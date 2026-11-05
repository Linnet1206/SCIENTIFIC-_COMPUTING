from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline, interp1d


def main():
    hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
    temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
    linear = interp1d(hours, temperature, kind="linear")
    cubic = CubicSpline(hours, temperature)
    sample_times = np.linspace(8.0, 14.0, 37)

    print(f"Linear estimate at 10:30: {float(linear(10.5)):.2f} C")
    print(f"Cubic estimate at 10:30: {float(cubic(10.5)):.2f} C")
    print(
        f"Changed target time to 11:30: linear={float(linear(11.5)):.2f} C, cubic={float(cubic(11.5)):.2f} C"
    )

    output_dir = Path(__file__).resolve().parents[1] / "outputs"
    output_dir.mkdir(exist_ok=True)
    plt.scatter(hours, temperature, label="Hourly measurements", color="black")
    plt.plot(sample_times, linear(sample_times), label="Linear")
    plt.plot(sample_times, cubic(sample_times), label="Cubic spline")
    plt.xlabel("Hour of day")
    plt.ylabel("Temperature (C)")
    plt.title("Temperature interpolation")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "task_13_interpolation.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Plot saved to outputs/task_13_interpolation.png")


if __name__ == "__main__":
    main()
