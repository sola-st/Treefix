# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
shape = pfor_input.unstacked_input(1)
new_shape = array_ops.concat([pfor_input.pfor.loop_len_vector, shape], axis=0)

# Expand dims of stacked t to broadcast against the new shape.
# TODO(davmre): consider factoring out common code with
# `expanddim_inputs_for_broadcast`, which has similar logic but with
# implicit shapes (of input Tensors) rather than explicit shapes.
rank_diff = array_ops.shape(new_shape)[0] - array_ops.rank(t)
ones = array_ops.tile([1], array_ops.reshape(rank_diff, [1]))
t_shape = array_ops.shape(t)
t_expanded_shape = array_ops.concat([t_shape[:1], ones, t_shape[1:]], axis=0)

exit(wrap(
    array_ops.broadcast_to(array_ops.reshape(t, t_expanded_shape), new_shape),
    True))
