# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
c = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args
for t in [np.float32, np.float64]:
    # where_v2 only
    with self.subTest(t=t):
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1, 1, 1) * 100
        self._compareGradientX(array_ops.where_v2, c, x.astype(t), y.astype(t))
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1, 3, 1) * 100
        self._compareGradientX(array_ops.where_v2, c, x.astype(t), y.astype(t))
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1, 1, 2) * 100
        self._compareGradientX(array_ops.where_v2, c, x.astype(t), y.astype(t))
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1, 1) * 100
        self._compareGradientX(array_ops.where_v2, c, x.astype(t), y.astype(t))
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1) * 100
        self._compareGradientX(array_ops.where_v2, c, x.astype(t), y.astype(t))
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(1, 2) * 100
        self._compareGradientX(array_ops.where_v2, c, x.astype(t), y.astype(t))
        x = np.random.rand(1, 3, 2) * 100
        y = np.random.rand(3, 2) * 100
        self._compareGradientX(array_ops.where_v2, c, x.astype(t), y.astype(t))
