# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
np.random.seed(127)  # Repeatable results
self._testLarge(np.float32)
self._testLarge(np.float64)
self._testLarge(np.complex64)
self._testLarge(np.complex128)
