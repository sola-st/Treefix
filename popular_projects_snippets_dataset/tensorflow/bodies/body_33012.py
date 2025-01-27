# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
num_rows = array_ops.shape(l)[-1]
batch_shape = array_ops.shape(l)[:-2]
l_inverse = linalg_ops.matrix_triangular_solve(l,
                                               linalg_ops.eye(
                                                   num_rows,
                                                   batch_shape=batch_shape,
                                                   dtype=l.dtype))
exit(_GradWithInverseL(l, l_inverse, grad))
