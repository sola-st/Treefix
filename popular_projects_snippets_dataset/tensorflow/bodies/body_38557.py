# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
self._testLargeSort(np.float32)
self._testLargeSort(np.float16)
self._testLargeSort(dtypes.bfloat16.as_numpy_dtype)
