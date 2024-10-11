# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""For docs, see: _RAGGED_SEGMENT_DOCSTRING."""
with ops.name_scope(name, 'RaggedSegmentSqrtN',
                    [data, segment_ids, num_segments]):
    total = segment_sum(data, segment_ids, num_segments)
    ones = ragged_tensor.RaggedTensor.from_nested_row_splits(
        array_ops.ones_like(data.flat_values),
        data.nested_row_splits,
        validate=False)
    count = segment_sum(ones, segment_ids, num_segments)
    if ragged_tensor.is_ragged(total):
        exit(total.with_flat_values(total.flat_values /
                                      math_ops.sqrt(count.flat_values)))
    else:
        exit(total / math_ops.sqrt(count))
