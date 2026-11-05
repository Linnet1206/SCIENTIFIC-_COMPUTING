from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def euler_cooling(step_size, ambient=25.0, initial=90.0, rate=0.12, end_time=30.0):
    time = np.arange(0.0, end_time + step_size / 2.0, step_size)
    temperature = np.empty_like(time)
    temperature[0] = initial
    for index in range(len(time) - 1):
        temperature[index + 1] = temperature[index] - step_size * rate * (
            temperature[index] - ambient
        )
    return time, temperature


def main():
    time, baseline = euler_cooling(1.0)
    _, finer = euler_cooling(0.5)
    exact = 25.0 + (90.0 - 25.0) * np.exp(-0.12 * time)
    finer_exact = 25.0 + (90.0 - 25.0) * np.exp(
        -0.12 * np.arange(0.0, 30.0 + 0.25, 0.5)
    )
    print(f"Euler final temperature (h=1 min): {baseline[-1]:.2f} C")
    print(f"Exact final temperature: {exact[-1]:.2f} C")
    print(f"Final absolute error (h=1): {abs(baseline[-1] - exact[-1]):.4f} C")
    print(
        f"Changed step to 0.5 min: final error={abs(finer[-1] - finer_exact[-1]):.4f} C"
    )

    output_dir = Path(__file__).resolve().parents[1] / "outputs"
    output_dir.mkdir(exist_ok=True)
    plt.plot(time, baseline, marker="o", markevery=5, label="Euler h=1 min")
    plt.plot(np.arange(0.0, 30.0 + 0.25, 0.5), finer, label="Euler h=0.5 min")
    plt.plot(time, exact, linestyle="--", label="Exact")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Temperature (C)")
    plt.title("Cooling of a hot object")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "task_17_euler_ode.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Plot saved to outputs/task_17_euler_ode.png")


if __name__ == "__main__":
    main()
