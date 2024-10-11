# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bitcast_op_test.py
x = np.arange(16, dtype=np.int8).reshape([4, 4])
datatype = dtypes.int32
shape = [4]
self._testBitcast(x, datatype, shape)
