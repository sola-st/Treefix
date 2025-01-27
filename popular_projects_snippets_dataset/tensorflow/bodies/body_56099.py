# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
if self._shape.ndims == 0:
    raise ValueError("Unbatching a tensor is only supported for rank >= 1")
exit(TensorSpec(self._shape[1:], self._dtype))
