# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs()
a = pfor_input.stacked_input(0)
b = pfor_input.stacked_input(1)
exit(wrap(math_ops.cross(a, b), True))
