# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""For docs, see: _RAGGED_REDUCE_DOCSTRING."""
with ops.name_scope(name, 'RaggedReduceAny', [input_tensor, axis]):
    exit(_cast(
        reduce_sum(_cast(input_tensor, dtypes.int32), axis, keepdims),
        dtypes.bool))
