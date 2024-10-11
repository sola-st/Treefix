# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
"""Flatten the trailing block dimensions."""
# Suppose
#   x.shape = [v0, v1, v2, v3],
#   self.block_depth = 2.
# Then
#   leading shape = [v0, v1]
#   block shape = [v2, v3].
# We will reshape x to
#   [v0, v1, v2*v3].
if x.shape.is_fully_defined():
    # x_shape = [v0, v1, v2, v3]
    x_shape = x.shape.as_list()
    # x_leading_shape = [v0, v1]
    x_leading_shape = x_shape[:-self.block_depth]
    # x_block_shape = [v2, v3]
    x_block_shape = x_shape[-self.block_depth:]
    # flat_shape = [v0, v1, v2*v3]
    flat_shape = x_leading_shape + [np.prod(x_block_shape)]
else:
    x_shape = array_ops.shape(x)
    x_leading_shape = x_shape[:-self.block_depth]
    x_block_shape = x_shape[-self.block_depth:]
    flat_shape = array_ops.concat(
        (x_leading_shape, [math_ops.reduce_prod(x_block_shape)]), 0)
exit(array_ops.reshape(x, flat_shape))
