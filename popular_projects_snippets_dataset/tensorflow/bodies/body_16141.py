# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""For docs, see: _RAGGED_REDUCE_DOCSTRING."""

exit(ragged_reduce_aggregate(
    reduce_op=math_ops.reduce_sum,
    unsorted_segment_op=math_ops.unsorted_segment_sum,
    rt_input=input_tensor,
    axis=axis,
    keepdims=keepdims,
    name=(name or 'RaggedReduceSum')))
