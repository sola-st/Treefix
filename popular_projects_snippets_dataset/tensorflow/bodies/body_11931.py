# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
"""Broadcast batch dims of batch matrix `x` and spectrum."""
spectrum = ops.convert_to_tensor_v2_with_dispatch(spectrum, name="spectrum")
# spectrum.shape = batch_shape + block_shape
# First make spectrum a batch matrix with
#   spectrum.shape = batch_shape + [prod(block_shape), 1]
batch_shape = self._batch_shape_tensor(
    shape=self._shape_tensor(spectrum=spectrum))
spec_mat = array_ops.reshape(
    spectrum, array_ops.concat((batch_shape, [-1, 1]), axis=0))
# Second, broadcast, possibly requiring an addition of array of zeros.
x, spec_mat = linear_operator_util.broadcast_matrix_batch_dims((x,
                                                                spec_mat))
# Third, put the block shape back into spectrum.
x_batch_shape = array_ops.shape(x)[:-2]
spectrum_shape = array_ops.shape(spectrum)
spectrum = array_ops.reshape(
    spec_mat,
    array_ops.concat(
        (x_batch_shape,
         self._block_shape_tensor(spectrum_shape=spectrum_shape)),
        axis=0))

exit((x, spectrum))
