# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bitcast_op_test.py
x = np.random.rand(3, 4)
shape = [3, 4]
self._testBitcast(x, dtypes.int64, shape)
