import numpy as np


def estimate_speed(time, position):
    return np.gradient(position, time, edge_order=2)


def main():
    time = np.arange(0.0, 7.0)
    position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])
    speed = estimate_speed(time, position)
    calibrated_position = 1.05 * position
    calibrated_speed = estimate_speed(time, calibrated_position)

    for moment, distance, velocity in zip(time, position, speed):
        print(
            f"t={moment:.0f} s, position={distance:.1f} m, estimated speed={velocity:.2f} m/s"
        )
    print(
        f"\nChanged GPS calibration by +5%: speed at 3 s={calibrated_speed[3]:.2f} m/s"
    )


if __name__ == "__main__":
    main()
