# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x = np.arange(1, 13, 2).reshape(1, 3, 2).astype(np.int32)
y = np.arange(1, 7, 1).reshape(1, 3, 2).astype(np.int32)
self._compareBoth(x, y, np.add, math_ops.add)
self._compareBoth(x, y, np.subtract, math_ops.subtract)
self._compareBoth(x, y, np.multiply, math_ops.multiply)
self._compareBoth(x, y, np.true_divide, math_ops.truediv)
self._compareBoth(x, y, np.floor_divide, math_ops.floordiv)
self._compareBoth(x, y, np.mod, math_ops.mod)
self._compareBoth(x, y, np.add, _ADD)
self._compareBoth(x, y, np.subtract, _SUB)
self._compareBoth(x, y, np.multiply, _MUL)
self._compareBoth(x, y, np.true_divide, _TRUEDIV)
self._compareBoth(x, y, np.floor_divide, _FLOORDIV)
self._compareBoth(x, y, np.mod, _MOD)
# _compareBoth tests on GPU only for floating point types, so test
# _MOD for int32 on GPU by calling _compareGpu
self._compareGpu(x, y, np.mod, _MOD)
