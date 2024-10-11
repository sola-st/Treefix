# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in test_dtypes:
    self._testBinary(
        op,
        np.array([[-0.25]], dtype=dtype),
        np.array([[8]], dtype=dtype),
        expected=np.array([[-2]], dtype=dtype))
    self._testBinary(
        op,
        np.array([[100, 10, 0.5]], dtype=dtype),
        np.array([[1, 3], [2, 5], [6, 8]], dtype=dtype),
        expected=np.array([[123, 354]], dtype=dtype))
    self._testBinary(
        op,
        np.array([[1, 3], [2, 5], [6, 8]], dtype=dtype),
        np.array([[100], [10]], dtype=dtype),
        expected=np.array([[130], [250], [680]], dtype=dtype))
    self._testBinary(
        op,
        np.array([[1000, 100], [10, 1]], dtype=dtype),
        np.array([[1, 2], [3, 4]], dtype=dtype),
        expected=np.array([[1300, 2400], [13, 24]], dtype=dtype))

    self._testBinary(
        op,
        np.array([], dtype=dtype).reshape((2, 0)),
        np.array([], dtype=dtype).reshape((0, 3)),
        expected=np.array([[0, 0, 0], [0, 0, 0]], dtype=dtype))
