# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
nums, divs = self.intTestData()
tf_result = math_ops.truncatemod(nums, divs)
np_result = np.fmod(nums, divs)
self.assertAllEqual(tf_result, np_result)
