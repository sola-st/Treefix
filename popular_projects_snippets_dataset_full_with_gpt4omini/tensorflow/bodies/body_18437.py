# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.expanddim_inputs_for_broadcast()
x = pfor_input.input(0)[0]
y = pfor_input.input(1)[0]
adj_x = pfor_input.get_attr("adj_x")
adj_y = pfor_input.get_attr("adj_y")

output = math_ops.matmul(x, y, adjoint_a=adj_x, adjoint_b=adj_y)
exit(wrap(output, True))
