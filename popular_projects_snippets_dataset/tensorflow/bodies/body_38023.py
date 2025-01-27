# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
dtypes = [
    np.float16,
    np.float32,
    np.float64,
    np.int8,
    np.int16,
    np.int32,
    np.int64,
    np.uint8,
    np.uint16,
    np.uint32,
    np.uint64,
    np.bool_,
]
x = np.asarray([0, 1, 2, 3, 4])
y = np.asarray([0, 1, 2, 3, 4])
for dtype in dtypes:
    xt = x.astype(dtype)
    yt = y.astype(dtype)
    cmp_eq = math_ops.equal(xt, yt)
    cmp_ne = math_ops.not_equal(xt, yt)
    values = self.evaluate([cmp_eq, cmp_ne])
    self.assertAllEqual(
        [[True, True, True, True, True], [False, False, False, False, False]],
        values)
for dtype in [np.complex64, np.complex128]:
    xt = x.astype(dtype)
    xt -= 1j * xt
    yt = y.astype(dtype)
    yt -= 1j * yt
    cmp_eq = math_ops.equal(xt, yt)
    cmp_ne = math_ops.not_equal(xt, yt)
    values = self.evaluate([cmp_eq, cmp_ne])
    self.assertAllEqual(
        [[True, True, True, True, True], [False, False, False, False, False]],
        values)
