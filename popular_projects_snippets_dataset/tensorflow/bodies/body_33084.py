# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/slicing_test.py
event_dim = 3
sliced = slicing._slice_single_param(
    array_ops.zeros([1, 1, event_dim]),
    param_ndims_to_matrix_ndims=1,
    slices=make_slices[44:-52:-3, -94::],
    batch_shape=constant_op.constant([2, 7], dtype=dtypes.int32))
self.assertAllEqual((1, 1, event_dim), self.evaluate(sliced).shape)
