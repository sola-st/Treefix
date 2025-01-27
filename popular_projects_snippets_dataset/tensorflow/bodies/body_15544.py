# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_row_splits_to_segment_ids_op_test.py
self.assertRaisesRegex(ValueError, r'Invalid row_splits: \[\]',
                       segment_id_ops.row_splits_to_segment_ids, [])
self.assertRaisesRegex(ValueError, r'splits must have dtype int32 or int64',
                       segment_id_ops.row_splits_to_segment_ids,
                       constant_op.constant([0.5]))
self.assertRaisesRegex(ValueError, r'Shape \(\) must have rank 1',
                       segment_id_ops.row_splits_to_segment_ids, 0)
self.assertRaisesRegex(ValueError, r'Shape \(1, 1\) must have rank 1',
                       segment_id_ops.row_splits_to_segment_ids, [[0]])
