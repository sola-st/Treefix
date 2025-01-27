# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Create variables for iteratively slicing a dense gradients tensor."""
# Since shape is 1-D, shape_of_shape = [rank-of-inputs]
shape_of_shape = array_ops.shape(sizes[0])
# Make a vector of length equal to the input's dimensions,
# with 0's everywhere and 1 in the concat dim position.
# Note: Can't use sparse_to_dense since it isn't GPU-capable (for now)
mask = array_ops.concat([
    array_ops.zeros(
        array_ops.expand_dims(concat_dim, 0), dtype=dtypes.int32), [1],
    array_ops.zeros(shape_of_shape - concat_dim - 1, dtype=dtypes.int32)
], 0)
begin = array_ops.zeros(shape_of_shape, dtype=dtypes.int32)
exit((mask, begin))
