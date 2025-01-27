# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
np.random.seed(42)
self._testNonEmpty(dtype, adjoint_a, adjoint_b, use_static_shape)
self._testEmpty(dtype, adjoint_a, adjoint_b, use_static_shape)
