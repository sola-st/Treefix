# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_segment_op_test.py
rt = ragged_factory_ops.constant([
    [[111, 112, 113, 114], [121]],  # row 0
    [],                             # row 1
    [[], [321, 322], [331]],        # row 2
    [[411, 412]]                    # row 3
])  # pyformat: disable
segment_ids = ragged_factory_ops.constant([[1, 2], [1], [1, 1, 2], [2]])

# Error is raised at graph-building time if we can detect it then.
self.assertRaisesRegex(
    errors.InvalidArgumentError,
    'segment_ids.shape must be a prefix of data.shape.*',
    ragged_math_ops.segment_sum, rt, segment_ids, 3)

# Otherwise, error is raised when we run the graph.
segment_ids2 = ragged_tensor.RaggedTensor.from_row_splits(
    array_ops.placeholder_with_default(segment_ids.values, None),
    array_ops.placeholder_with_default(segment_ids.row_splits, None))
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    'segment_ids.shape must be a prefix of data.shape.*'):
    self.evaluate(ragged_math_ops.segment_sum(rt, segment_ids2, 3))
