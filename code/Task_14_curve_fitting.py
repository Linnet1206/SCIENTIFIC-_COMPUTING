from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def response_model(users, quadratic, linear, intercept):
    return quadratic * users**2 + linear * users + intercept


def fit_response(users, response_ms):
    parameters, _ = curve_fit(response_model, users, response_ms)
    predictions = response_model(users, *parameters)
    rmse = np.sqrt(np.mean((response_ms - predictions) ** 2))
    return parameters, rmse


def main():
    users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
    response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)
    parameters, rmse = fit_response(users, response_ms)
    print(f"Fitted coefficients (quadratic, linear, intercept): {parameters}")
    print(f"Training RMSE: {rmse:.2f} ms")
    print(f"Predicted response at 400 users: {response_model(400, *parameters):.2f} ms")
    print(
        f"Changed load to 450 users: predicted response={response_model(450, *parameters):.2f} ms"
    )

    output_dir = Path(__file__).resolve().parents[1] / "outputs"
    output_dir.mkdir(exist_ok=True)
    users_plot = np.linspace(users.min(), 450.0, 300)
    plt.scatter(users, response_ms, label="Measurements")
    plt.plot(users_plot, response_model(users_plot, *parameters), label="Quadratic fit")
    plt.xlabel("Concurrent users")
    plt.ylabel("Response time (ms)")
    plt.title("Server response-time curve fitting")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_dir / "task_14_curve_fitting.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Plot saved to outputs/task_14_curve_fitting.png")


if __name__ == "__main__":
    main()
