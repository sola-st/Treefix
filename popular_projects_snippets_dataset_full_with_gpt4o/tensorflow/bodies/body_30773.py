# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bitcast_op_test.py
x = np.random.rand(3, 2)
datatype = dtypes.int8
shape = [3, 2, 8]
self._testBitcast(x, datatype, shape)
