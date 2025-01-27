# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
exit(x + random_ops.random_uniform(
    (), 0, 2, dtype=dtypes.int64, seed=1))
