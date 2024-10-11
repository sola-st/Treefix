# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
x = np.empty((0, 0, 0, 0), dtype=np.float32)
self._testBothReshape(x, [1, 2, 3, 0])
self._testBothReshape(x, [1, 0, 0, 4])
self._testBothReshape(x, [0, 0, 0, 0])
self._testBothReshape(x, [1, 2, 0])
self._testBothReshape(x, [0, 0, 0])
self._testBothReshape(x, [1, -1, 5])
