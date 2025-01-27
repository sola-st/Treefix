# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bitcast_op_test.py
x = np.ones([], np.int32)
datatype = dtypes.int8
shape = [4]
self._testBitcast(x, datatype, shape)
