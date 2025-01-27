# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/dynamic_slice_ops_test.py
for dtype in self.numeric_types:
    self._assertOpOutputMatchesExpected(
        xla.dynamic_update_slice, [
            np.array([], dtype=dtype),
            np.array([], dtype=dtype),
            np.array([0], dtype=np.int32)
        ],
        expected=np.array([], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        xla.dynamic_update_slice, [
            np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=dtype),
            np.array([-1, -2, -3], dtype=dtype),
            np.array([6], dtype=np.int32)
        ],
        expected=np.array([1, 2, 3, 4, 5, 6, -1, -2, -3, 10], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        xla.dynamic_update_slice, [
            np.array(
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=dtype),
            np.array([[42, 43], [44, 45]], dtype=dtype),
            np.array([1, 2], dtype=np.int32)
        ],
        expected=np.array(
            [[1, 2, 3, 4], [5, 6, 42, 43], [9, 10, 44, 45]], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        xla.dynamic_update_slice, [
            np.array(
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=dtype),
            np.array([[], []], dtype=dtype),
            np.array([1, 2], dtype=np.int32)
        ],
        expected=np.array(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        xla.dynamic_update_slice, [
            np.array(
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=dtype),
            np.ones([3, 4], dtype=dtype),
            np.array([0, 0], dtype=np.int32)
        ],
        expected=np.ones([3, 4], dtype=dtype))
