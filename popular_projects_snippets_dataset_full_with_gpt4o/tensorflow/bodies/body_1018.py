# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/segment_reduction_ops_test.py
for dtype in self.numeric_types:
    data = np.ones((4, 8, 7), dtype=dtype)
    indices = np.ones((3, 2), dtype=np.int32)
    num_segments = 4
    self.assertRaises(
        ValueError,
        functools.partial(self._segmentReduction,
                          math_ops.unsorted_segment_sum, data, indices,
                          num_segments))
