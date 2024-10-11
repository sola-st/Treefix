# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
shapes = [
    ([1, 3, 2], [1]),
    ([1, 3, 2], [2]),
    ([1, 3, 2], [3, 2]),
    ([1, 3, 2], [3, 1]),
    ([1, 3, 2], [1, 3, 2]),
    ([1, 3, 2], [2, 3, 1]),
    ([1, 3, 2], [2, 1, 1]),
    ([1, 3, 2], [1, 3, 1]),
    ([2, 1, 5], [2, 3, 1]),
    ([2, 0, 5], [2, 0, 1]),
    ([2, 3, 0], [2, 3, 1]),
]
dtypes = [
    np.float16,
    np.float32,
    np.float64,
    np.int32,
    np.int64,
]
if include_complex:
    dtypes.extend([np.complex64, np.complex128])

for (xs, ys) in shapes:
    for dtype in dtypes:
        self._compareBCast(xs, ys, dtype, np_func, tf_func)
