# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
with ops.control_dependencies([prev]):
    exit((t + 1, sparse_ops.sparse_tensor_dense_matmul(
        sp_x, y, adjoint_a=adjoint_a, adjoint_b=adjoint_b)))
