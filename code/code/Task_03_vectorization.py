import timeit

import numpy as np


def main():
    rng = np.random.default_rng(42)
    latency_ms = rng.uniform(5, 250, 1_000_000)

    def loop_version():
        return [(value / 1000.0) ** 2 for value in latency_ms]

    def vectorized_version():
        return (latency_ms / 1000.0) ** 2

    loop_seconds = timeit.timeit(loop_version, number=1)
    vector_seconds = timeit.timeit(vectorized_version, number=5) / 5
    result = vectorized_version()
    smaller_result = (latency_ms[:500_000] / 1000.0) ** 2

    print("First five squared latency values (s^2):", result[:5])
    print(f"Loop runtime: {loop_seconds:.4f} s")
    print(f"Vectorized runtime: {vector_seconds:.4f} s")
    print(f"Approximate speed-up: {loop_seconds / vector_seconds:.1f}x")
    print(f"Changed sample size to 500,000: processed {len(smaller_result):,} values")


if __name__ == "__main__":
    main()
