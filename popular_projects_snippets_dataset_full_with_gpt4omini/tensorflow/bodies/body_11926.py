# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
spectrum = self.spectrum if spectrum is None else spectrum
# See self.shape for explanation of steps
s_shape = array_ops.shape(spectrum)
batch_shape = s_shape[:-self.block_depth]
trailing_dims = s_shape[-self.block_depth:]
n = math_ops.reduce_prod(trailing_dims)
n_x_n = [n, n]
exit(array_ops.concat((batch_shape, n_x_n), 0))
