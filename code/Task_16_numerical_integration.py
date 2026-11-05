import numpy as np
from scipy.integrate import simpson


def estimate_energy(time_hours, power_kw):
    return np.trapezoid(power_kw, time_hours), simpson(power_kw, x=time_hours)


def main():
    time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
    power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
    trapezoid, simpson_estimate = estimate_energy(time_hours, power_kw)
    changed_trapezoid, changed_simpson = estimate_energy(time_hours, 1.1 * power_kw)

    print(f"Trapezoidal energy: {trapezoid:.3f} kWh")
    print(f"Simpson energy: {simpson_estimate:.3f} kWh")
    print(f"Difference between methods: {abs(simpson_estimate - trapezoid):.3f} kWh")
    print("\nParameter change: all power readings increase by 10%")
    print(f"Trapezoidal energy: {changed_trapezoid:.3f} kWh")
    print(f"Simpson energy: {changed_simpson:.3f} kWh")


if __name__ == "__main__":
    main()
