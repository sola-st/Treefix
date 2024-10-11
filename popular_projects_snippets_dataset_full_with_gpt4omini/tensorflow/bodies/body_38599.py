# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
self._compare(
    np.arange(0, 21).reshape([3, 7]).astype(dtypes.bfloat16.as_numpy_dtype))
self._compare(
    np.arange(0, 210).reshape([2, 3, 5,
                               7]).astype(dtypes.bfloat16.as_numpy_dtype))
self._compare(
    np.arange(0, 16).reshape([1, 2, 1, 2, 1, 2, 1,
                              2]).astype(dtypes.bfloat16.as_numpy_dtype))
