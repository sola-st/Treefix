# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs()
t = pfor_input.stacked_input(0)
diag = pfor_input.stacked_input(1)
exit(wrap(array_ops.matrix_set_diag(t, diag), True))
