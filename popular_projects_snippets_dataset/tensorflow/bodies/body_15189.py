# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_segment_op_test.py
dt = constant_op.constant([1, 2, 3, 4, 5, 6])
segment_ids = ragged_factory_ops.constant([[1, 2], []])
self.assertRaisesRegex(
    ValueError, 'segment_ids.shape must be a prefix of data.shape, '
    'but segment_ids is ragged and data is not.',
    ragged_math_ops.segment_sum, dt, segment_ids, 3)
