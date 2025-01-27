# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_segment_ids_to_row_splits_op_test.py
self.assertRaisesRegex(
    TypeError,
    r'Argument `tensor` \(name\: segment_ids\) must be of type integer.*',
    segment_id_ops.segment_ids_to_row_splits, constant_op.constant([0.5]))
self.assertRaisesRegex(ValueError, r'Shape \(\) must have rank 1',
                       segment_id_ops.segment_ids_to_row_splits, 0)
self.assertRaisesRegex(ValueError, r'Shape \(1, 1\) must have rank 1',
                       segment_id_ops.segment_ids_to_row_splits, [[0]])
