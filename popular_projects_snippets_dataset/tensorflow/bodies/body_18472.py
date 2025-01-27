# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
exit([wrap(x, True) for x in linalg_ops.log_matrix_determinant(t)])
