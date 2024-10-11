# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/noop_elimination_test.py
const = constant_op.constant(-1, dtype=dtypes.int64)
exit(ds.map(lambda x: (x, const)))
