# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
for t in (np.float16, np.float32, np.float64, np.int32, np.int64,
          np.complex64, np.complex128):
    with self.subTest(t=t):
        self._compareDiffType(2, t, False)
        self._compareDiffType(3, t, False)

        x = [1, 2, 3]
        y = [4, 5]

        a = [[1, 1], [1, 1]]

        self._compareDiff(x, y, False)
        self._compareDiff(x, a, False)
