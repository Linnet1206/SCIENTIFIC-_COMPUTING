from scipy.optimize import root_scalar


def net_present_value(rate, cash_flows):
    if rate <= -1.0:
        raise ValueError("Rate must be greater than -100%")
    return sum(flow / (1.0 + rate) ** year for year, flow in enumerate(cash_flows))


def derivative_npv(rate, cash_flows):
    return sum(
        -year * flow / (1.0 + rate) ** (year + 1)
        for year, flow in enumerate(cash_flows)
        if year
    )


def find_irr(cash_flows):
    newton = root_scalar(
        net_present_value,
        args=(cash_flows,),
        fprime=derivative_npv,
        x0=0.10,
        method="newton",
        xtol=1e-12,
    )
    secant = root_scalar(
        net_present_value,
        args=(cash_flows,),
        x0=0.05,
        x1=0.20,
        method="secant",
        xtol=1e-12,
    )
    return newton, secant


def main():
    cash_flows = [-10000.0, 3000.0, 3500.0, 4000.0, 2500.0]
    newton, secant = find_irr(cash_flows)
    print(f"IRR using Newton-Raphson: {newton.root:.6%}")
    print(f"IRR using secant method: {secant.root:.6%}")
    print(f"NPV at Newton solution: {net_present_value(newton.root, cash_flows):.6f}")

    changed_flows = cash_flows.copy()
    changed_flows[-1] += 500.0
    changed_newton, _ = find_irr(changed_flows)
    print(f"\nChanged final inflow from 2500 to 3000: IRR={changed_newton.root:.6%}")


if __name__ == "__main__":
    main()
