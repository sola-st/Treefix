# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/slicing_test.py
param = array_ops.placeholder_with_default(
    array_ops.zeros([7, 6, 5, 4, 3]), shape=None)
idx = array_ops.placeholder_with_default(
    constant_op.constant(2, dtype=dtypes.int32), shape=[])
sliced = slicing._slice_single_param(
    param,
    param_ndims_to_matrix_ndims=2,
    slices=make_slices[:, idx],
    batch_shape=constant_op.constant([7, 6, 5]))
self.assertAllEqual((7, 5, 4, 3), self.evaluate(sliced).shape)
