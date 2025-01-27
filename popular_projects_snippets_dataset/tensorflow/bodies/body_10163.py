# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
int64_t_max = 2**63 - 1
x = math_ops.range(0, 201, int64_t_max - 200, dtype=dtypes.int64)
self.assertAllEqual((0,), self.evaluate(x))  # just below potential overflow
x = math_ops.range(0, 202, int64_t_max - 200, dtype=dtypes.int64)
self.assertAllEqual(
    (0,), self.evaluate(x))  # smallest input with potential overflow
