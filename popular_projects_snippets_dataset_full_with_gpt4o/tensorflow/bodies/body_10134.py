# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
"""Edge-case test data for integer types."""
# INT_MIN/-1 expected to produce signed-integer overflow,
# INT_MIN/INT_MAX expected to work.
nums = np.array([np.iinfo(dtype).min, -1, 1,
                 np.iinfo(dtype).max],
                dtype=dtype).reshape([4, 1])
divs = nums.reshape([1, 4])
exit((nums, divs))
