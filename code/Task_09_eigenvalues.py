import numpy as np


def centrality_scores(adjacency):
    eigenvalues, eigenvectors = np.linalg.eigh(adjacency)
    index = np.argmax(eigenvalues)
    vector = np.abs(eigenvectors[:, index])
    return eigenvalues[index], vector / vector.sum(), vector


def main():
    adjacency = np.array(
        [
            [0.0, 1.0, 1.0, 0.0],
            [1.0, 0.0, 1.0, 1.0],
            [1.0, 1.0, 0.0, 1.0],
            [0.0, 1.0, 1.0, 0.0],
        ]
    )
    nodes = ["A", "B", "C", "D"]
    dominant_value, scores, vector = centrality_scores(adjacency)
    print(f"Dominant eigenvalue: {dominant_value:.6f}")
    print("Node importance:")
    for node, score in zip(nodes, scores):
        print(f"{node}: {score:.4f}")
    print(
        f"Eigenpair verification error: {np.linalg.norm(adjacency @ vector - dominant_value * vector):.2e}"
    )

    changed_adjacency = adjacency.copy()
    changed_adjacency[0, 3] = changed_adjacency[3, 0] = 1.0
    _, changed_scores, _ = centrality_scores(changed_adjacency)
    print("\nParameter change: add a connection between A and D")
    for node, score in zip(nodes, changed_scores):
        print(f"{node}: {score:.4f}")


if __name__ == "__main__":
    main()
