# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/segment_reduction_ops_test.py
for dtype in self.numeric_types:
    data = np.array(
        [[0, 1, 2, 3], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43],
         [50, 51, 52, 53]],
        dtype=dtype)
    indices = np.array([0, 1, 2, 0, 1], dtype=np.int32)
    num_segments = 4
    y = self._unsortedSegmentSum(data, indices, num_segments)
    self.assertAllClose(
        np.array(
            [[40, 42, 44, 46], [70, 72, 74, 76], [30, 31, 32, 33],
             [0, 0, 0, 0]],
            dtype=dtype), y)
