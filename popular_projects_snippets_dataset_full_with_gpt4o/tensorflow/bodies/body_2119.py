# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/manip_ops_test.py
for t in self.float_types:
    self._testRoll(np.random.rand(5).astype(t), 2, 0)
    self._testRoll(np.random.rand(3, 4).astype(t), [1, 2], [1, 0])
    self._testRoll(np.random.rand(1, 3, 4).astype(t), [1, 0, -3], [0, 1, 2])
