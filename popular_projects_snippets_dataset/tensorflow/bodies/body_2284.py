# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.all_types:
    x = np.random.randint(0, high=100, size=[2, 3])
    self._testBinary(
        array_ops.broadcast_to,
        x,
        np.array([2, 3], dtype=np.int32),
        expected=x)
    self._testBinary(
        array_ops.broadcast_to,
        np.zeros([2, 3], dtype=dtype),
        np.array([2, 2, 3], dtype=np.int32),
        expected=np.zeros([2, 2, 3], dtype=dtype))

    x = np.arange(2).reshape((2, 1)).astype(dtype)
    self._testBinary(
        array_ops.broadcast_to,
        x,
        np.array([2, 2, 3], dtype=np.int32),
        expected=np.tile(x, (2, 1, 3)))

    x = np.arange(3).reshape((3, 1, 1, 1)).astype(dtype)
    self._testBinary(
        array_ops.broadcast_to,
        x,
        np.array((3, 7, 8, 9), dtype=np.int32),
        expected=np.tile(x, (1, 7, 8, 9)))
