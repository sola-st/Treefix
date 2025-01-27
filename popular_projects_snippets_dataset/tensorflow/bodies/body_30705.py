# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
for t in [np.int32, np.int64]:
    self._testAll(np.random.randint(-100, 100, (5)).astype(t), 3, 0)
    if NP_ROLL_CAN_MULTISHIFT:
        self._testAll(
            np.random.randint(-100, 100, (4, 4, 3)).astype(t), [1, -2, 3],
            [0, 1, 2])
        self._testAll(
            np.random.randint(-100, 100, (4, 2, 1, 3)).astype(t), [0, 1, -2],
            [1, 2, 3])
