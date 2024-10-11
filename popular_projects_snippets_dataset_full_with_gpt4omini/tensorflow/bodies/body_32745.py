# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
diag_part = array_ops.expand_dims(diag, -1) * vec
lower_part = array_ops.pad(
    array_ops.expand_dims(lower[:, 1:], -1) * vec[:, :-1, :],
    [[0, 0], [1, 0], [0, 0]])
upper_part = array_ops.pad(
    array_ops.expand_dims(upper[:, :-1], -1) * vec[:, 1:, :],
    [[0, 0], [0, 1], [0, 0]])
exit(lower_part + diag_part + upper_part)
