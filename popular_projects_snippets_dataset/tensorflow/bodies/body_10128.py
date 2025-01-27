# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
nums, divs = self.floatTestData()
tf_result = math_ops.realdiv(nums, divs)
np_result = np.divide(nums, divs)
self.assertAllClose(tf_result, np_result)
