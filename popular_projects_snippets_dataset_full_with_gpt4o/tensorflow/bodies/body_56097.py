# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
if batched and self._shape.merge_with(value.shape).ndims == 0:
    raise ValueError("Unbatching a tensor is only supported for rank >= 1")
exit(self._to_components(value))
