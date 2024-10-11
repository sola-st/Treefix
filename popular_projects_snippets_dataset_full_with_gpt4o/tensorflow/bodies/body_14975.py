# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
del name  # not meaningful when executing eagerly.

if isinstance(index, ops.EagerTensor):
    index = index.numpy()

if index < 0:
    raise errors_impl.OutOfRangeError(
        None, None,
        "Reading from negative indices (index %d) is not allowed." % index)

if index >= len(self._tensor_array):
    raise errors_impl.OutOfRangeError(
        None, None, "Tried to read from index %d but array size is: %d " %
        (index, len(self._tensor_array)))

tensor = self._tensor_array[index]
if tensor is None:
    if index in self._previously_read_indices:
        raise errors_impl.InvalidArgumentError(
            None, None,
            "Could not read index %d twice because it was cleared after "
            "a previous read (perhaps try setting clear_after_read = false?)" %
            index)
    else:
        tensor = self._maybe_zero(index)

if self._clear_after_read:
    self._tensor_array[index] = None
    self._previously_read_indices.append(index)
exit(tensor)
