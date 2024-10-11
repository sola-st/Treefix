# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.numeric_types:
    self._testBinary(
        array_ops.expand_dims,
        dtype(7),
        np.int32(0),
        expected=np.array([7], dtype=dtype))
    self._testBinary(
        array_ops.expand_dims,
        np.array([42], dtype=dtype),
        np.array([0], dtype=np.int64),
        expected=np.array([[42]], dtype=dtype))
    self._testBinary(
        array_ops.expand_dims,
        np.array([], dtype=dtype),
        np.int32(0),
        expected=np.array([[]], dtype=dtype))
    self._testBinary(
        array_ops.expand_dims,
        np.array([[[1, 2], [3, 4]]], dtype=dtype),
        np.int32(0),
        expected=np.array([[[[1, 2], [3, 4]]]], dtype=dtype))
    self._testBinary(
        array_ops.expand_dims,
        np.array([[[1, 2], [3, 4]]], dtype=dtype),
        np.int32(1),
        expected=np.array([[[[1, 2], [3, 4]]]], dtype=dtype))
    self._testBinary(
        array_ops.expand_dims,
        np.array([[[1, 2], [3, 4]]], dtype=dtype),
        np.int32(2),
        expected=np.array([[[[1, 2]], [[3, 4]]]], dtype=dtype))
    self._testBinary(
        array_ops.expand_dims,
        np.array([[[1, 2], [3, 4]]], dtype=dtype),
        np.int32(3),
        expected=np.array([[[[1], [2]], [[3], [4]]]], dtype=dtype))
    self._testBinary(
        array_ops.expand_dims,
        np.array([[[1, 2], [3, 4]]], dtype=dtype),
        np.array([2], dtype=np.int64),
        expected=np.array([[[[1, 2]], [[3, 4]]]], dtype=dtype))
