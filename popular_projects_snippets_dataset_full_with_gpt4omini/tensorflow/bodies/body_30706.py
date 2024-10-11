# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
for t in [np.float32, np.float64, dtypes.bfloat16.as_numpy_dtype]:
    self._testAll(np.random.rand(5).astype(t), 2, 0)
    if NP_ROLL_CAN_MULTISHIFT:
        self._testAll(np.random.rand(3, 4).astype(t), [1, 2], [1, 0])
        self._testAll(np.random.rand(1, 3, 4).astype(t), [1, 0, -3], [0, 1, 2])
