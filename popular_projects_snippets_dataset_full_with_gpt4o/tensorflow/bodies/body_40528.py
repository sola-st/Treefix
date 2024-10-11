# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
t = math_ops._as_indexed_slices(
    constant_op.constant([[1., 2.], [0, 0], [3., 4.]]))
result = backprop_util.AggregateIndexedSlicesGradients([t])
self._assert_indexed_slices_equal(t, result)
