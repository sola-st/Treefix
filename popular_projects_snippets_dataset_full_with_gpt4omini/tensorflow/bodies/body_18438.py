# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
indices = pfor_input.unstacked_input(1)
# Shift positive indices by one to account for the extra dimension.
indices += math_ops.cast(indices >= 0, indices.dtype)
keep_dims = pfor_input.get_attr("keep_dims")
exit(wrap(op_func(t, indices, keepdims=keep_dims), True))
