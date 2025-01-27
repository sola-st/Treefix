# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
self._testSimpleDtype(dtypes.bfloat16.as_numpy_dtype)
self._testSimpleDtype(np.float16)
self._testSimpleDtype(np.float32)
self._testSimpleDtype(np.float64)
self._testSimpleDtype(np.int32)
self._testSimpleDtype(np.int64)
self._testSimpleDtype(np.complex64)
self._testSimpleDtype(np.complex128)
self._testSimpleDtype("|S")  # byte strings in python2 + 3
