# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable([0., 0., 0., 0.])
self.assertAllEqual(
    v.scatter_nd_sub([[3], [1]], [1., 2.], name="sub"), [0., -2., 0., -1.])
self.assertAllEqual(
    v.scatter_nd_add([[2], [0]], [1., 2.], name="add"), [2., -2., 1., -1.])
self.assertAllEqual(
    v.scatter_nd_update([[1], [3]], [3., 3.], name="update"),
    [2., 3., 1., 3.])
