# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_segment_ids_to_row_splits_op_test.py
segment_ids = [0, 0, 0, 2, 2, 3, 4, 4, 4]
num_segments = 7
expected = [0, 3, 3, 5, 6, 9, 9, 9]
splits = segment_id_ops.segment_ids_to_row_splits(segment_ids, num_segments)
self.assertAllEqual(splits, expected)
