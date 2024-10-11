# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
for t in [np.float16, np.float32, np.float64]:
    self._testElu(np.array([-1, np.nan, 1, np.nan]).astype(t))
