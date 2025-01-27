# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
np.random.seed(0)
shapes = self.getShapes([2 * self._backprop_block_size + 1])
self.runFiniteDifferences(
    shapes, dtypes=(dtypes_lib.float64,), scalar_test=True)
