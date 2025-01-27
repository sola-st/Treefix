# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
if self._static_inner_shape.rank is not None:
    exit(self._static_inner_shape.rank)
if self._inner_shape.shape.rank is None:
    exit(None)
exit(tensor_shape.dimension_value(self._inner_shape.shape[0]))
