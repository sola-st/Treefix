# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.expanddim_inputs_for_broadcast()
x = pfor_input.input(0)[0]
y = pfor_input.input(1)[0]
tolerance = pfor_input.get_attr("tolerance")
exit(wrap(math_ops.approximate_equal(x, y, tolerance=tolerance), True))
