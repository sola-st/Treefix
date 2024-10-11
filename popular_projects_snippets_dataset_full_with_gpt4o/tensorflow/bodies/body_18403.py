# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
dims = pfor_input.unstacked_input(0)
value = pfor_input.stacked_input(1)
# Expand the rank of `value`
new_shape = array_ops.concat(
    [[-1], array_ops.ones([array_ops.size(dims)], dtype=dtypes.int32)],
    axis=0)
value = array_ops.reshape(value, new_shape)
# Compute the new output shape
new_dims = array_ops.concat([pfor_input.pfor.loop_len_vector, dims], axis=0)
# Broadcast
exit(wrap(array_ops.broadcast_to(value, new_dims), True))
