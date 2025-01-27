# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
if self._shape.ndims == 0:
    raise ValueError("Unbatching a tensor is only supported for rank >= 1")
exit(SparseTensorSpec(self._shape[1:], self._dtype))
