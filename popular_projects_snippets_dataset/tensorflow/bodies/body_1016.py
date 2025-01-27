# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/segment_reduction_ops_test.py
for dtype in self.numeric_types:
    data = np.array(
        [[[0, 1, 2], [10, 11, 12]], [[100, 101, 102], [110, 111, 112]], [[
            200, 201, 202
        ], [210, 211, 212]], [[300, 301, 302], [310, 311, 312]]],
        dtype=dtype)
    indices = np.array([[3, 5], [3, 1], [5, 0], [6, 2]], dtype=np.int32)
    num_segments = 8
    y = self._unsortedSegmentSum(data, indices, num_segments)
    self.assertAllClose(
        np.array(
            [[210, 211, 212], [110, 111, 112], [310, 311, 312], [
                100, 102, 104
            ], [0, 0, 0.], [210, 212, 214], [300, 301, 302], [0, 0, 0]],
            dtype=dtype), y)
