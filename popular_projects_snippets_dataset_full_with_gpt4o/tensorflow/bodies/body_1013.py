# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/segment_reduction_ops_test.py
for dtype in self.numeric_types:
    self.assertAllClose(
        np.array([6, 3, 0, 6], dtype=dtype),
        self._unsortedSegmentSum(
            np.array([0, 1, 2, 3, 4, 5, 6], dtype=dtype),
            np.array([3, -1, 0, 1, 0, -1, 3], dtype=np.int32), 4))
