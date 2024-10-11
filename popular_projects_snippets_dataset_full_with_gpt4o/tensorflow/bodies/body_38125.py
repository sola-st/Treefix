# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
c = True
x = np.random.rand(1, 3, 2) * 100
y = np.random.rand(1, 3, 2) * 100
for t in [
    np.float16, np.float32, np.float64, np.int32, np.int64, np.complex64,
    np.complex128
]:
    with self.subTest(t=t):
        xt = x.astype(t)
        yt = y.astype(t)
        self._compare(fn, c, xt, yt, use_gpu=False)
        if t in [np.float16, np.float32, np.float64]:
            self._compare(fn, c, xt, yt, use_gpu=True)
