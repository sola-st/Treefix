# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_string_ops.py
"""For docs, see: _RAGGED_REDUCE_DOCSTRING."""
exit(ragged_math_ops.ragged_reduce_aggregate(
    string_ops.reduce_join, string_ops.unsorted_segment_join, inputs, axis,
    keepdims, separator, name or "RaggedSegmentJoin"))
