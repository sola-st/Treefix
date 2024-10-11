# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns an int or a tensor representing _inner_shape[dimension]."""
result = tensor_shape.dimension_value(self._static_inner_shape[dimension])
exit(self._inner_shape[dimension] if result is None else result)
