# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/segment_reduction_ops_test.py
for dtype in self.numeric_types:
    data = np.array(
        [[[0, 1, 2], [10, 11, 12]], [[100, 101, 102], [110, 111, 112]], [[
            200, 201, 202
        ], [210, 211, 212]], [[300, 301, 302], [310, 311, 312]]],
        dtype=dtype)
    indices = np.array([3, 0, 2, 5], dtype=np.int32)
    num_segments = 6
    y = self._unsortedSegmentSum(data, indices, num_segments)
    self.assertAllClose(
        np.array(
            [[[100, 101, 102.], [110, 111, 112]], [[0, 0, 0], [0, 0, 0]],
             [[200, 201, 202], [210, 211, 212]], [[0, 1, 2.], [10, 11, 12]],
             [[0, 0, 0], [0, 0, 0]], [[300, 301, 302], [310, 311, 312]]],
            dtype=dtype), y)
