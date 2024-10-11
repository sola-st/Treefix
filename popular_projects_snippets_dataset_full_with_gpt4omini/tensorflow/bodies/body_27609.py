# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
exit(((x[0] * x[1] + math_ops.cast(y, dtypes.float32)) / (
    x[1] + 1), x[1] + 1))
