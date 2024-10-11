# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/slicing_test.py
sliced = slicing._slice_single_param(
    array_ops.zeros([7, 6, 5, 4, 3]),
    param_ndims_to_matrix_ndims=2,
    slices=make_slices[:, 2:],
    batch_shape=constant_op.constant([7, 6, 5]))
self.assertAllEqual((7, 4, 5, 4, 3), self.evaluate(sliced).shape)
