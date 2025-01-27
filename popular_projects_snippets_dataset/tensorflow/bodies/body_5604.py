# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable([[1., 2.], [3., 4.]])
self.assertAllEqual(
    v.sparse_read([1, 0], name="read"), [[3., 4.], [1., 2.]])
self.assertAllEqual(
    v.gather_nd([[1, 0], [0, 1]], name="gather_nd"), [3., 2.])
