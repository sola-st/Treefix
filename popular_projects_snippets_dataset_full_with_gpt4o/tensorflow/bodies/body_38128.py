# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
c = True
# where_v2 only
x = np.random.rand(1, 3, 2) * 100
y = np.random.rand(1, 1, 1) * 100
self._testScalarBroadcast(array_ops.where_v2, c, x, y)
self._testScalarBroadcast(array_ops.where_v2, c, y, x)
x = np.random.rand(1, 3, 2) * 100
y = np.random.rand(1, 3, 1) * 100
self._testScalarBroadcast(array_ops.where_v2, c, x, y)
self._testScalarBroadcast(array_ops.where_v2, c, y, x)
x = np.random.rand(1, 3, 2) * 100
y = np.random.rand(1, 1, 2) * 100
self._testScalarBroadcast(array_ops.where_v2, c, x, y)
self._testScalarBroadcast(array_ops.where_v2, c, y, x)
x = np.random.rand(1, 3, 2) * 100
y = np.random.rand(1, 1) * 100
self._testScalarBroadcast(array_ops.where_v2, c, x, y)
self._testScalarBroadcast(array_ops.where_v2, c, y, x)
x = np.random.rand(1, 3, 2) * 100
y = np.random.rand(1) * 100
self._testScalarBroadcast(array_ops.where_v2, c, x, y)
self._testScalarBroadcast(array_ops.where_v2, c, y, x)
x = np.random.rand(1, 3, 2) * 100
y = np.random.rand(1, 2) * 100
self._testScalarBroadcast(array_ops.where_v2, c, x, y)
self._testScalarBroadcast(array_ops.where_v2, c, y, x)
x = np.random.rand(1, 3, 2) * 100
y = np.random.rand(3, 2) * 100
self._testScalarBroadcast(array_ops.where_v2, c, x, y)
self._testScalarBroadcast(array_ops.where_v2, c, y, x)
