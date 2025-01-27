# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
dtypes = [
    dtypes_lib.qint8,
    dtypes_lib.qint16,
    dtypes_lib.quint8,
    dtypes_lib.quint16,
    dtypes_lib.qint32,
]
x = np.asarray([0, 1, 2, 3, 4])
y = np.asarray([0, 1, 2, 3, 4])
for dtype in dtypes:
    xt = x.astype(dtype.as_numpy_dtype)
    yt = y.astype(dtype.as_numpy_dtype)
    cmp_eq = math_ops.equal(xt, yt)
    cmp_ne = math_ops.not_equal(xt, yt)
    values = self.evaluate([cmp_eq, cmp_ne])
    self.assertAllEqual(
        [[True, True, True, True, True], [False, False, False, False, False]],
        values)
