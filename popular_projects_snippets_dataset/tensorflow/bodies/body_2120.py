# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/manip_ops_test.py
for t in self.complex_types:
    x = np.random.rand(4, 4).astype(t)
    self._testRoll(x + 1j * x, 2, 0)
    x = np.random.rand(2, 5).astype(t)
    self._testRoll(x + 1j * x, [1, 2], [1, 0])
    x = np.random.rand(3, 2, 1, 1).astype(t)
    self._testRoll(x + 1j * x, [2, 1, 1, 0], [0, 3, 1, 2])
