# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
nums, divs = self.floatTestData()
tf_result = math_ops.truncatediv(nums, divs)
np_result = np.trunc(nums / divs)
self.assertAllEqual(tf_result, np_result)
