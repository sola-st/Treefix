# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
s_shape = self._spectrum.shape
# Suppose spectrum.shape = [a, b, c, d]
# block_depth = 2
# Then:
#   batch_shape = [a, b]
#   N = c*d
# and we want to return
#   [a, b, c*d, c*d]
batch_shape = s_shape[:-self.block_depth]
# trailing_dims = [c, d]
trailing_dims = s_shape[-self.block_depth:]
if trailing_dims.is_fully_defined():
    n = np.prod(trailing_dims.as_list())
else:
    n = None
n_x_n = tensor_shape.TensorShape([n, n])
exit(batch_shape.concatenate(n_x_n))
