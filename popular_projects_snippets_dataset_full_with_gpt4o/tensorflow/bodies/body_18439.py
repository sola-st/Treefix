# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
dimension = pfor_input.unstacked_input(1)
dimension += math_ops.cast(dimension >= 0, dimension.dtype)
output_type = pfor_input.get_attr("output_type")
exit(wrap(op_func(t, axis=dimension, output_type=output_type), True))
