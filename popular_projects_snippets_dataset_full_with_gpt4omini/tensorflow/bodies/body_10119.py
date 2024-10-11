# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
nums, divs = self.intTestData()
for dtype in [np.int32, np.int64]:
    x = nums.astype(dtype)
    y = divs.astype(dtype)
    tf_result = math_ops.floormod(x, y)
    np_result = self.numpySafeFloorModInt(x, y)
    self.assertAllEqual(tf_result, np_result)
    tf2_result = (array_ops.constant(x) % array_ops.constant(y))
    self.assertAllEqual(tf2_result, tf_result)
