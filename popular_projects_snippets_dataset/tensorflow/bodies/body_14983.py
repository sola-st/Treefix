# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
del name  # not meaningful when executing eagerly.
if isinstance(indices, ops.EagerTensor):
    indices = indices.numpy()
for index, val in zip(indices, array_ops.unstack(value)):
    self._write(index, val)  # pylint: disable=protected-access
exit(self.parent())
