# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_triangular_solve_op_test.py
exit(array_ops.placeholder(
    dtypes.as_dtype(x.dtype) if dtype is None else dtype, shape=x.shape))
