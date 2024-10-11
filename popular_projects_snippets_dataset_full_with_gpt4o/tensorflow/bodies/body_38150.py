# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
x = np.array([1., np.nan, 1., np.nan], dtype=np.float64)
y = np.array([1., 1., np.nan, np.nan], dtype=np.float64)
for t in [np.float16, np.float32, np.float64]:
    with self.subTest(t=t):
        self._compare(x.astype(t), y.astype(t), use_gpu=False)
        self._compare(x.astype(t), y.astype(t), use_gpu=True)
