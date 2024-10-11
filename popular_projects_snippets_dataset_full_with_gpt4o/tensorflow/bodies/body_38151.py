# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
x = np.random.rand(1, 3, 2) * 100.
y = np.random.rand(2) * 100.  # should broadcast
for t in [np.float16, np.float32, np.float64, np.int32, np.int64]:
    with self.subTest(t=t):
        self._compare(x.astype(t), y.astype(t), use_gpu=False)
        self._compare(x.astype(t), y.astype(t), use_gpu=True)
