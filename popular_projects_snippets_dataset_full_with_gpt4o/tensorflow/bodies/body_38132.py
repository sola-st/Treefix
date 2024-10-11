# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
c0 = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args
c1 = np.random.randint(0, 2, 2).astype(np.bool_).reshape(1, 1, 2)  # pylint: disable=too-many-function-args
c2 = np.random.randint(0, 2, 3).astype(np.bool_).reshape(1, 3, 1)  # pylint: disable=too-many-function-args
c3 = np.random.randint(0, 2, 1).astype(np.bool_).reshape(1, 1, 1)  # pylint: disable=too-many-function-args
for c in [c0, c1, c2, c3]:
    # where_v2 only
    with self.subTest(c=c):
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1, 1, 1) * 100
        self._testBasicBroadcast(array_ops.where_v2, c, x, y)
        self._testBasicBroadcast(array_ops.where_v2, c, y, x)
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1, 3, 1) * 100
        self._testBasicBroadcast(array_ops.where_v2, c, x, y)
        self._testBasicBroadcast(array_ops.where_v2, c, y, x)
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1, 1, 2) * 100
        self._testBasicBroadcast(array_ops.where_v2, c, x, y)
        self._testBasicBroadcast(array_ops.where_v2, c, y, x)
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1, 1) * 100
        self._testBasicBroadcast(array_ops.where_v2, c, x, y)
        self._testBasicBroadcast(array_ops.where_v2, c, y, x)
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1) * 100
        self._testBasicBroadcast(array_ops.where_v2, c, x, y)
        self._testBasicBroadcast(array_ops.where_v2, c, y, x)
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1, 2) * 100
        self._testBasicBroadcast(array_ops.where_v2, c, x, y)
        self._testBasicBroadcast(array_ops.where_v2, c, y, x)
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(3, 2) * 100
        self._testBasicBroadcast(array_ops.where_v2, c, x, y)
        self._testBasicBroadcast(array_ops.where_v2, c, y, x)
