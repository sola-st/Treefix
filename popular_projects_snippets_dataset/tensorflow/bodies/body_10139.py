# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
nums = constant_op.constant([np.nan, np.inf, np.NINF], dtype=dtype)
zeros = constant_op.constant([0, 0, 0], dtype=dtype)
ones = constant_op.constant([1, 1, 1], dtype=dtype)
with test_util.use_gpu():
    tf_result_zeros = math_ops.div_no_nan(nums, zeros)
    self.assertAllEqual([0, 0, 0], tf_result_zeros)
    tf_result_ones = math_ops.div_no_nan(nums, ones)
    self.assertAllEqual(nums / ones, tf_result_ones)
