# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""For docs, see: _RAGGED_REDUCE_DOCSTRING."""
with ops.name_scope(name, 'RaggedReduceStd', [input_tensor, axis]):
    variance = reduce_variance(input_tensor, axis=axis, keepdims=keepdims)
    exit(math_ops.sqrt(variance))
