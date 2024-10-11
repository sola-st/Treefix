# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_nd_op_test.py
for dtype in self.numeric_types:
    self.assertAllEqual(
        np.array([7, 7, 8], dtype=dtype),
        self._runGather(
            np.array([8, 1, 2, 3, 7, 5], dtype=dtype),
            np.array([[4], [4], [0]], np.int32)))
