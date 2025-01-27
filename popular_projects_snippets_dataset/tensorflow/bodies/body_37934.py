# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
dtypes = [
    np.float16,
    np.float32,
    np.float64,
    np.int32,
    np.int64,
    np.complex64,
    np.complex128,
]
for dtype in dtypes:
    for (np_func, tf_func) in funcs:
        if (dtype in (np.complex64, np.complex128) and
            tf_func in (_FLOORDIV, math_ops.floordiv)):
            continue  # floordiv makes no sense for complex numbers
        self._compareBCast(xs, ys, dtype, np_func, tf_func)
        self._compareBCast(ys, xs, dtype, np_func, tf_func)
