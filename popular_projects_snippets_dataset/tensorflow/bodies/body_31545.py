# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
for t in [np.int8, np.int16, np.int32, np.int64]:
    self._testAll(
        np.array([[10, 20, 30], [40, 50, 60]]).astype(t),
        np.array([1, 2, 3]).astype(t))
