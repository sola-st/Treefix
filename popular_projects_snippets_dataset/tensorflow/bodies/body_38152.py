# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
x = np.random.rand(1, 3, 2) * 100.
y = np.random.rand(1).item() * 100.  # should broadcast
# dropped np.float64, int64 because TF automatically converts to 32 bit
for t in [np.float32, np.int32]:
    with self.subTest(t=t):
        self._compare(x.astype(t), t(y), use_gpu=False)
        self._compare(x.astype(t), t(y), use_gpu=True)
