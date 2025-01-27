# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
# For docs, see: _RAGGED_SEGMENT_DOCSTRING
exit(_ragged_segment_aggregate(
    math_ops.unsorted_segment_sum,
    data=data,
    segment_ids=segment_ids,
    num_segments=num_segments,
    name=(name or 'RaggedSegmentSum')))
