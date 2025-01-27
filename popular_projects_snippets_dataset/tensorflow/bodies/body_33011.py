# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
l_inverse = linalg_ops.matrix_inverse(l)
exit(_GradWithInverseL(l, l_inverse, grad))
