# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
with ops.control_dependencies([prev]):
    exit((t + 1, math_ops.matmul(
        x,
        y,
        transpose_a=adjoint_a,
        transpose_b=adjoint_b,
        a_is_sparse=True,
        b_is_sparse=False)))
