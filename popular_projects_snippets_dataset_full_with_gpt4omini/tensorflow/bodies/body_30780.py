# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bitcast_op_test.py
shape = [3, 4]
x = np.zeros(shape, np.uint16)
datatype = dtypes.quint16
self._testBitcast(x, datatype, shape)
