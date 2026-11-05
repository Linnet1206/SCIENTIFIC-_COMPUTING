from scipy.optimize import minimize


def optimize_allocation(required_capacity):
    def cost(allocation):
        return 12.0 * allocation[0] + 18.0 * allocation[1]

    def capacity_constraint(allocation):
        return 100.0 * allocation[0] + 170.0 * allocation[1] - required_capacity

    result = minimize(
        cost,
        x0=[5.0, 3.0],
        method="SLSQP",
        bounds=[(0.0, None), (0.0, None)],
        constraints={"type": "ineq", "fun": capacity_constraint},
    )
    if not result.success:
        raise RuntimeError(result.message)
    return result


def main():
    for capacity in (1000.0, 1200.0):
        solution = optimize_allocation(capacity)
        type_a, type_b = solution.x
        actual_capacity = 100.0 * type_a + 170.0 * type_b
        print(f"Required capacity: {capacity:.0f}")
        print(f"Continuous allocation: A={type_a:.3f}, B={type_b:.3f}")
        print(f"Achieved capacity: {actual_capacity:.2f}; cost={solution.fun:.2f}")

    best_integer = min(
        (12 * type_a + 18 * type_b, type_a, type_b, 100 * type_a + 170 * type_b)
        for type_a in range(21)
        for type_b in range(21)
        if 100 * type_a + 170 * type_b >= 1000
    )
    print(
        "\nBest integer allocation for 1000 capacity (cost, A, B, capacity):",
        best_integer,
    )


if __name__ == "__main__":
    main()
