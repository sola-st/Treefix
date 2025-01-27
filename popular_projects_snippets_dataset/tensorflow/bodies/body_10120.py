# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
nums, divs = self.floatTestData()
for dtype in [np.float16, np.float32, np.float64]:
    x = nums.astype(dtype)
    y = divs.astype(dtype)
    tf_result = math_ops.floormod(x, y)
    np_result = x % y
    self.assertAllEqual(tf_result, np_result)
    tf2_result = (array_ops.constant(x) % array_ops.constant(y))
    self.assertAllEqual(tf2_result, tf_result)
