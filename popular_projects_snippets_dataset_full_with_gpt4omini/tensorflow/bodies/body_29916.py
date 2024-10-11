# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
x = np.zeros([0, 6]).astype(np.float32)
self._testBothReshape(x, [-1, 2, 3])
