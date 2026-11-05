from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def solve_circuit(
    supply_voltage, resistance=1000.0, capacitance=0.001, initial_voltage=0.0
):
    def derivative(_, voltage):
        return [(supply_voltage - voltage[0]) / (resistance * capacitance)]

    evaluation_times = np.linspace(0.0, 5.0, 200)
    return solve_ivp(
        derivative,
        (0.0, 5.0),
        [initial_voltage],
        t_eval=evaluation_times,
        rtol=1e-9,
        atol=1e-11,
    )


def main():
    baseline = solve_circuit(5.0)
    changed = solve_circuit(6.0)
    exact = 5.0 * (1.0 - np.exp(-baseline.t / (1000.0 * 0.001)))
    print("Solver success:", baseline.success)
    print(f"Voltage at 5 s with Vs=5 V: {baseline.y[0, -1]:.4f} V")
    print(
        f"Maximum error against exact solution: {np.max(np.abs(baseline.y[0] - exact)):.3e} V"
    )
    print(f"Changed supply to 6 V: voltage at 5 s={changed.y[0, -1]:.4f} V")

    output_dir = Path(__file__).resolve().parents[1] / "outputs"
    output_dir.mkdir(exist_ok=True)
    plt.plot(baseline.t, baseline.y[0], label="Supply 5 V")
    plt.plot(changed.t, changed.y[0], label="Supply 6 V")
    plt.plot(baseline.t, exact, linestyle="--", label="Exact (5 V)")
    plt.xlabel("Time (s)")
    plt.ylabel("Capacitor voltage (V)")
    plt.title("RC circuit charging")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "task_18_scipy_ode.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Plot saved to outputs/task_18_scipy_ode.png")


if __name__ == "__main__":
    main()
