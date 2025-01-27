# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
bfloat16 = dtypes_lib.bfloat16.as_numpy_dtype
self._testAll(np.arange(-15, 15).reshape([2, 3, 5]).astype(bfloat16))
self._testAll(
    np.random.normal(size=30).reshape([2, 3, 5]).astype(bfloat16))
self._testAll(np.empty((2, 0, 5)).astype(bfloat16))
