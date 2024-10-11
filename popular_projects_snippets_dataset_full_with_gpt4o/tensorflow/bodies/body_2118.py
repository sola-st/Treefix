# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/manip_ops_test.py
for t in self.numeric_types:
    self._testRoll(np.random.randint(-100, 100, (5)).astype(t), 3, 0)
    self._testRoll(
        np.random.randint(-100, 100, (4, 4, 3)).astype(t), [1, -6, 6],
        [0, 1, 2])
    self._testRoll(
        np.random.randint(-100, 100, (4, 2, 1, 3)).astype(t), [0, 1, -2],
        [1, 2, 3])
