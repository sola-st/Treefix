# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
nums, divs = self.floatTestData()
tf_result = math_ops.floormod(
    math_ops.cast(nums, dtypes.bfloat16),
    math_ops.cast(divs, dtypes.bfloat16))
np_result = nums % divs
self.assertAllEqual(tf_result, np_result)
