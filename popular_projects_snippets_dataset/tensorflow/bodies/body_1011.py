# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/segment_reduction_ops_test.py
for dtype in self.numeric_types:
    self.assertAllClose(
        np.array(
            [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5],
             [0, 0, 0, 0, 0, 0]],
            dtype=dtype),
        self._unsortedSegmentSum(
            np.array([0, 1, 2, 3, 4, 5], dtype=dtype), 2, 4))
