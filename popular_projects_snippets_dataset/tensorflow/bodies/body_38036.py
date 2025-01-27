# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
if kwargs["transpose_" + x_name] is True:
    exit(x.T)
elif kwargs["adjoint_" + x_name] is True:
    exit(np.conj(x.T))
else:
    exit(x)
