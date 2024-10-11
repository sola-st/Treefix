# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
shape = tensor_shape.TensorShape(pfor_input.get_attr("shape"))
exit(wrap(gen_array_ops.ensure_shape(t, [None] + shape), True))
