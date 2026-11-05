from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def estimate_overload(demand, capacity):
    overloaded = demand > capacity
    return overloaded.mean(), overloaded


def main():
    rng = np.random.default_rng(42)
    demand = rng.normal(850.0, 120.0, 100_000)
    baseline_probability, overloaded = estimate_overload(demand, 1000.0)
    changed_probability, _ = estimate_overload(demand, 950.0)
    print(
        f"Estimated overload probability at capacity 1000: {baseline_probability:.4%}"
    )
    print(f"Changed capacity to 950: overload probability={changed_probability:.4%}")
    print(
        f"Simulations: {len(demand):,}; overload events at capacity 1000: {overloaded.sum():,}"
    )

    output_dir = Path(__file__).resolve().parents[1] / "outputs"
    output_dir.mkdir(exist_ok=True)
    plt.hist(demand, bins=60, color="#3977a8", alpha=0.8)
    plt.axvline(1000.0, color="#b33b32", linestyle="--", label="Capacity 1000")
    plt.axvline(950.0, color="#d58a27", linestyle=":", label="Changed capacity 950")
    plt.xlabel("Simulated demand")
    plt.ylabel("Frequency")
    plt.title("Monte Carlo server-overload scenarios")
    plt.legend()
    plt.grid(axis="y", alpha=0.25)
    plt.savefig(output_dir / "task_20_monte_carlo.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Plot saved to outputs/task_20_monte_carlo.png")


if __name__ == "__main__":
    main()
