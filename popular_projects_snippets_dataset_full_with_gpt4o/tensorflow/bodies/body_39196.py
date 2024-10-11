# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
np.random.seed(127)  # Repeatable results
self._testBasic(np.int32)
self._testBasic(np.float16)
self._testBasic(np.float32)
self._testBasic(np.float64)
self._testBasic(np.complex64)
self._testBasic(np.complex128)
self._testBasic(np.int32, indices_dtype=np.int32)
self._testBasic(np.float32, indices_dtype=np.int32)
