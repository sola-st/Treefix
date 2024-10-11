# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
self._testLargeTopK(np.float32)
self._testLargeTopK(np.float16)
self._testLargeTopK(dtypes.bfloat16.as_numpy_dtype)
