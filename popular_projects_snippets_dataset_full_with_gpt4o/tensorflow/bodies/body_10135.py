# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [np.int32, np.int64]:
    x, y = self.intEdgeTestData(dtype)
    tf_floor_div = math_ops.floor_div(x, y)
    np_floor_div = self.numpySafeFloorDivInt(x, y)
    self.assertAllEqual(tf_floor_div, np_floor_div)
    tf_floor_mod = math_ops.floormod(x, y)
    np_floor_mod = self.numpySafeFloorModInt(x, y)
    self.assertAllEqual(tf_floor_mod, np_floor_mod)
    z = math_ops.add(math_ops.multiply(tf_floor_div, y), tf_floor_mod)
    # x = floor_div(x, y) * y + floor_mod(x, y)
    self.assertAllEqual(z, np.broadcast_to(x, z.shape))
