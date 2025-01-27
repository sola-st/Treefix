# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
adjoint = pfor_input.get_attr("adjoint")
exit(wrap(gen_linalg_ops.matrix_inverse(t, adjoint=adjoint), True))
