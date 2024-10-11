# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_segment_ids_to_row_splits_op_test.py
# Note: the splits for an empty ragged tensor contains a single zero.
segment_ids = segment_id_ops.segment_ids_to_row_splits([])
self.assertAllEqual(segment_ids, [0])
