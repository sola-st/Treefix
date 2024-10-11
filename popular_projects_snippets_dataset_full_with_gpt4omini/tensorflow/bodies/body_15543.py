# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_row_splits_to_segment_ids_op_test.py
# Note: the splits for an empty ragged tensor contains a single zero.
segment_ids = segment_id_ops.row_splits_to_segment_ids([0])
self.assertAllEqual(segment_ids, [])
