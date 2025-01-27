# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
for t in [self._qint8, self._quint8, self._qint32]:
    self._testAll(
        np.random.randint(-100, 100, (4, 4, 3)).astype(t),
        [[1, 0], [2, 3], [0, 2]], 0)
    self._testAll(
        np.random.randint(-100, 100, (4, 2, 1, 3)).astype(t),
        [[0, 0], [0, 0], [0, 0], [0, 0]],
        np.array(123).astype(t))
