# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
val = [compat.as_bytes(str(x)) for x in np.arange(-15, 15)]
self._testCpu(np.array(val).reshape([2, 3, 5]))
self._testCpu(np.empty((2, 0, 5)).astype(np.str_))
