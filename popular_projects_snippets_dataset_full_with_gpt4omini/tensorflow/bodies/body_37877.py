# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
# output's shape depends on adj[0] and adj[1]
if adjoint_a:
    x = np.conjugate(np.swapaxes(x, -1, -2))
if adjoint_b:
    y = np.conjugate(np.swapaxes(y, -1, -2))
exit(np.matmul(x, y))
