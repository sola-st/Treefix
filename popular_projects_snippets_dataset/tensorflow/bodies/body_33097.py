# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/slicing_test.py
sliced = slicing._slice_single_param(
    array_ops.zeros([4, 3, 1]),  # batch = [4, 3], event = [1]
    param_ndims_to_matrix_ndims=1,
    slices=make_slices[
        array_ops.newaxis, ..., array_ops.newaxis, 2:, array_ops.newaxis],
    batch_shape=constant_op.constant([7, 4, 3]))
expected = array_ops.zeros(
    [1, 4, 3])[
        array_ops.newaxis, ..., array_ops.newaxis,
        2:, array_ops.newaxis].shape + [1]
self.assertAllEqual(expected, self.evaluate(sliced).shape)
