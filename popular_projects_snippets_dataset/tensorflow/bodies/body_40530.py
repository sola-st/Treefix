# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
t0 = math_ops._as_indexed_slices(
    constant_op.constant([[1., 2.], [0, 0], [3., 4.]]))
t1 = math_ops._as_indexed_slices(
    constant_op.constant([[0., 0.], [5, 6], [7., 8.]]))
t3 = None
total = constant_op.constant([[1., 2.], [5, 6], [10., 12.]])
result = backprop_util.AggregateIndexedSlicesGradients([t0, t1, t3])
self._assert_indexed_slices_equal(total, result)
