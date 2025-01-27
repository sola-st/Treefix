# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_segment_op_test.py
rt_as_list = [[0, 1, 2, 3], [4], [], [5, 6], [7], [8, 9]]
rt = ragged_factory_ops.constant(rt_as_list)
num_segments = max(segment_ids) + 1
expected = self.expected_value(rt_as_list, segment_ids, num_segments,
                               combiner)

segmented = segment_op(rt, segment_ids, num_segments)
self.assertAllEqual(segmented, expected)
