# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
np.random.seed(42)
x = GetRandomNormalInput(a_shape, dtype)
y = GetRandomNormalInput(b_shape, dtype)
self._checkGrad(x, y, adjoint_a, adjoint_b)
