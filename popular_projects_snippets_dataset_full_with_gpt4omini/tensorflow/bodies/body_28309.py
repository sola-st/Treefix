# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
exit(random_ops.random_uniform(
    (), 0, 10, dtype=dtypes.int32) * math_ops.cast(x, dtypes.int32))
