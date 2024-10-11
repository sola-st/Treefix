# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.expanddim_inputs_for_broadcast()
x = pfor_input.input(0)[0]
y = pfor_input.input(1)[0]
incompatible_shape_error = pfor_input.get_attr("incompatible_shape_error")
exit(wrap(gen_math_ops.not_equal(
    x, y, incompatible_shape_error=incompatible_shape_error), True))
