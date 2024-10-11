# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_grad_test.py
np.random.seed(5)  # Fix seed to avoid flakiness
self._testGradientsType(np.float16, np.int64)
self._testGradientsType(np.float32, np.int64)
self._testGradientsType(np.float64, np.int64)
self._testGradientsType(np.complex64, np.int64)
self._testGradientsType(np.complex128, np.int64)
self._testGradientsType(np.float32, np.int32)
self._testGradientsType(np.complex64, np.int32)
