# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_segment_ids_to_row_splits_op_test.py
# Segment ids are not required to be sorted.
segment_ids = [0, 4, 3, 2, 4, 4, 2, 0, 0]
splits1 = segment_id_ops.segment_ids_to_row_splits(segment_ids)
expected1 = [0, 3, 3, 5, 6, 9]

splits2 = segment_id_ops.segment_ids_to_row_splits(segment_ids, 7)
expected2 = [0, 3, 3, 5, 6, 9, 9, 9]
self.assertAllEqual(splits1, expected1)
self.assertAllEqual(splits2, expected2)
