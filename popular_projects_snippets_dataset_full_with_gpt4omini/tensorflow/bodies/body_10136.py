# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [np.int32, np.int64]:
    x, y = self.intEdgeTestData(dtype)
    tf_truncate_div = math_ops.truncatediv(x, y)
    np_truncate_div = self.numpySafeTruncateDivInt(x, y)
    self.assertAllEqual(tf_truncate_div, np_truncate_div)
    tf_truncate_mod = math_ops.truncatemod(x, y)
    np_truncate_mod = self.numpySafeTruncateModInt(x, y)
    self.assertAllEqual(tf_truncate_mod, np_truncate_mod)
    z = math_ops.add(math_ops.multiply(tf_truncate_div, y), tf_truncate_mod)
    # x = truncatediv(x, y) * y + truncatemod(x, y)
    self.assertAllEqual(z, np.broadcast_to(x, z.shape))
