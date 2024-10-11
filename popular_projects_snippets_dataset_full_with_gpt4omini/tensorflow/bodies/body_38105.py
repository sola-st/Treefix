# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
x = np.linspace(-15, 15, 6).reshape(1, 3, 2)  # pylint: disable=too-many-function-args
y = np.linspace(20, -10, 6).reshape(1, 3, 2)  # pylint: disable=too-many-function-args
for t in [np.float16, np.float32, np.float64, np.int32, np.int64]:
    with self.subTest(t=t):
        xt = x.astype(t)
        yt = y.astype(t)
        self._compare(xt, yt, np.less, math_ops.less)
        self._compare(xt, yt, np.less_equal, math_ops.less_equal)
        self._compare(xt, yt, np.greater, math_ops.greater)
        self._compare(xt, yt, np.greater_equal, math_ops.greater_equal)
        self._compare(xt, yt, np.equal, math_ops.equal)
        self._compare(xt, yt, np.not_equal, math_ops.not_equal)
    # Complex types do not support ordering but do support equality tests.
for t in [np.complex64, np.complex128]:
    with self.subTest(t=t):
        xt = x.astype(t)
        xt -= 1j * xt
        yt = y.astype(t)
        yt -= 1j * yt
        self._compare(xt, yt, np.equal, math_ops.equal)
        self._compare(xt, yt, np.not_equal, math_ops.not_equal)
