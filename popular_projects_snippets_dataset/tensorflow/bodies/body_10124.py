# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
nums, divs = self.intTestData()
tf_result = math_ops.floor_div(nums, divs)
np_result = self.numpySafeFloorDivInt(nums, divs)
self.assertAllEqual(tf_result, np_result)
tf2_result = (array_ops.constant(nums) // array_ops.constant(divs))
self.assertAllEqual(tf2_result, tf_result)
