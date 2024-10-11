# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable([0., 0., 0.])
self.assertAllEqual(
    v.scatter_add(
        _make_index_slices(values=[1., 2.], indices=[0, 2]),
        use_locking=True,
        name="add"), [1., 0., 2.])
self.assertAllEqual(
    v.scatter_div(
        _make_index_slices(values=[4., 2.], indices=[0, 2]),
        use_locking=True,
        name="div"), [0.25, 0., 1.])
self.assertAllEqual(
    v.scatter_max(
        _make_index_slices(values=[1., 0.5], indices=[1, 2]),
        use_locking=True,
        name="max"), [0.25, 1., 1.])
self.assertAllEqual(
    v.scatter_min(
        _make_index_slices(values=[1., 0.5], indices=[0, 1]),
        use_locking=True,
        name="min"), [0.25, 0.5, 1.])
self.assertAllEqual(
    v.scatter_mul(
        _make_index_slices(values=[2., 0.5], indices=[0, 1]),
        use_locking=True,
        name="mul"), [0.5, 0.25, 1.])
self.assertAllEqual(
    v.scatter_sub(
        _make_index_slices(values=[2., 0.5], indices=[0, 1]),
        use_locking=True,
        name="sub"), [-1.5, -0.25, 1.])
self.assertAllEqual(
    v.scatter_update(
        _make_index_slices(values=[2., 0.5], indices=[0, 1]),
        use_locking=True,
        name="update"), [2., 0.5, 1.])
self.assertAllEqual(
    v.batch_scatter_update(
        _make_index_slices(values=[1., 1.5], indices=[0, 1]),
        use_locking=True,
        name="update"), [1., 1.5, 1.])
