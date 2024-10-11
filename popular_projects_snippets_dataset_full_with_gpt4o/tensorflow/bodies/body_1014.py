# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/segment_reduction_ops_test.py
for dtype in self.numeric_types:
    data = np.array(
        [[0, 1, 2, 3], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43],
         [50, 51, 52, 53]],
        dtype=dtype)
    indices = np.array([8, 1, 0, 3, 7], dtype=np.int32)
    num_segments = 10
    y = self._unsortedSegmentSum(data, indices, num_segments)
    self.assertAllClose(
        np.array(
            [[30, 31, 32, 33], [20, 21, 22, 23], [0, 0, 0, 0],
             [40, 41, 42, 43], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
             [50, 51, 52, 53], [0, 1, 2, 3], [0, 0, 0, 0]],
            dtype=dtype), y)
