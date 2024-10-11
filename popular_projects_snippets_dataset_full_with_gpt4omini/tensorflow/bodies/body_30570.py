# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
# Test case for GitHub issue 35710
tf_ans = math_ops.range(
    constant_op.constant(4, dtype=dtypes.int32), dtype=dtypes.int64)
self.assertAllEqual(self.evaluate(tf_ans), np.array([0, 1, 2, 3]))
