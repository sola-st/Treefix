# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
self._testMediumTopK(np.float32)
self._testMediumTopK(np.float16)
self._testMediumTopK(dtypes.bfloat16.as_numpy_dtype)
