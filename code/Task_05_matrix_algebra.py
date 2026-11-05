import numpy as np


def transform_points(angle_degrees):
    points = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])
    angle = np.deg2rad(angle_degrees)
    rotation = np.array(
        [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
    )
    scale = np.diag([2.0, 1.5])
    transformation = rotation @ scale
    return points, transformation, points @ transformation.T


def main():
    points, transformation, baseline = transform_points(45.0)
    _, _, changed = transform_points(30.0)
    print("Original square points:\n", points)
    print("Combined scale-and-rotate matrix:\n", transformation)
    print("Transformed points at 45 degrees:\n", baseline)
    print(f"Transformation determinant: {np.linalg.det(transformation):.4f}")
    print("\nParameter change: rotation 45 to 30 degrees")
    print("First transformed point at 30 degrees:", changed[1])


if __name__ == "__main__":
    main()
