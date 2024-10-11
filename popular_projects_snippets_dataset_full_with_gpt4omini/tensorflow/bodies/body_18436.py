# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# TODO(agarwal): There may be a more efficient way to do this instead of
# stacking the inputs.
pfor_input.stack_inputs()
x = pfor_input.stacked_input(0)
y = pfor_input.stacked_input(1)
adj_x = pfor_input.get_attr("adj_x")
adj_y = pfor_input.get_attr("adj_y")

x = _flatten_first_two_dims(x)
y = _flatten_first_two_dims(y)
output = math_ops.matmul(x, y, adjoint_a=adj_x, adjoint_b=adj_y)
output = _unflatten_first_dim(output, pfor_input.pfor.loop_len_vector)
exit(wrap(output, True))
