from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root_scalar


def heat_balance(temperature, heat_gain=10.0):
    return temperature - 25.0 - heat_gain * np.exp(-temperature / 20.0)


def fixed_point(heat_gain, initial=30.0, tolerance=1e-10, max_iterations=500):
    estimate = initial
    for iteration in range(1, max_iterations + 1):
        updated = 25.0 + heat_gain * np.exp(-estimate / 20.0)
        if abs(updated - estimate) < tolerance:
            return updated, iteration
        estimate = updated
    raise RuntimeError("Fixed-point iteration did not converge")


def main():
    solution = root_scalar(
        heat_balance, args=(10.0,), bracket=(20.0, 40.0), method="bisect", xtol=1e-10
    )
    fixed_temperature, iterations = fixed_point(10.0)
    changed = root_scalar(
        heat_balance, args=(12.0,), bracket=(20.0, 45.0), method="bisect", xtol=1e-10
    )
    print(f"Bisection equilibrium: {solution.root:.6f} C")
    print(
        f"Fixed-point equilibrium: {fixed_temperature:.6f} C in {iterations} iterations"
    )
    print(f"Residual at bisection root: {heat_balance(solution.root):.2e}")
    print(f"Changed heat gain from 10 to 12: equilibrium={changed.root:.6f} C")

    output_dir = Path(__file__).resolve().parents[1] / "outputs"
    output_dir.mkdir(exist_ok=True)
    temperatures = np.linspace(20.0, 45.0, 300)
    plt.plot(temperatures, heat_balance(temperatures), label="Heat gain 10")
    plt.axhline(0.0, color="black", linewidth=0.8)
    plt.axvline(solution.root, linestyle="--", label=f"Root {solution.root:.2f} C")
    plt.xlabel("Temperature (C)")
    plt.ylabel("Heat-balance residual")
    plt.title("Heat-balance equilibrium")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "task_10_root_finding.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Plot saved to outputs/task_10_root_finding.png")


if __name__ == "__main__":
    main()
