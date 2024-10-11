# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs()
matrix = pfor_input.stacked_input(0)
rhs = pfor_input.stacked_input(1)
adjoint = pfor_input.get_attr("adjoint")
output = gen_linalg_ops.matrix_solve(
    matrix, rhs, adjoint=adjoint)
exit(wrap(output, True))
