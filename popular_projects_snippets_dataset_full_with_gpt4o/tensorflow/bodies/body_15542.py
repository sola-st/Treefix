# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_row_splits_to_segment_ids_op_test.py
splits = [0, 3, 3, 5, 6, 9]
expected = [0, 0, 0, 2, 2, 3, 4, 4, 4]
segment_ids = segment_id_ops.row_splits_to_segment_ids(splits)
self.assertAllEqual(segment_ids, expected)
