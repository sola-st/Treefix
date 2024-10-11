# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.expanddim_inputs_for_broadcast()
matrix = pfor_input.input(0)[0]
rhs = pfor_input.input(1)[0]
lower = pfor_input.get_attr("lower")
adjoint = pfor_input.get_attr("adjoint")
output = linalg_ops.matrix_triangular_solve(
    matrix, rhs, lower=lower, adjoint=adjoint)
exit(wrap(output, True))
