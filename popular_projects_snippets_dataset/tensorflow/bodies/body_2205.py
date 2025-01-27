# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_matmul_ops_test.py
super_pad = [[0, 0], [0, 1], [1, 0]]
sub_pad = [[0, 0], [1, 0], [0, 1]]

super_part = array_ops.pad(array_ops.matrix_diag(superdiag), super_pad)
main_part = array_ops.matrix_diag(maindiag)
sub_part = array_ops.pad(array_ops.matrix_diag(subdiag), sub_pad)
exit(super_part + main_part + sub_part)
