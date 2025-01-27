# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
nums = np.arange(-10, 10, .25).reshape(80, 1)
divs = np.arange(-3, 3, .25).reshape(1, 24)

tf_nums = constant_op.constant(nums, dtype=dtype)
tf_divs = constant_op.constant(divs, dtype=dtype)

# Use tf versions for expected value to ensure inputs are identical
# (e.g. in the case of bfloat16).
np_nums = self.evaluate(tf_nums)
np_divs = self.evaluate(tf_divs)
np_result = np.true_divide(np_nums, np_divs)
np_result[:, np_divs[0] == 0] = 0

with test_util.use_gpu():
    tf_result = math_ops.div_no_nan(tf_nums, tf_divs)
    self.assertAllCloseAccordingToType(tf_result, np_result)
