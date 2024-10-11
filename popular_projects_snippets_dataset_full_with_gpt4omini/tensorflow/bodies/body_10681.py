# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Return the value to return from a get op.

    If the staging area has names, return a dictionary with the
    names as keys.  Otherwise return either a single tensor
    or a list of tensors depending on the length of `tensors`.

    Args:
      tensors: List of tensors from the get op.
      indices: Indices of associated names and shapes

    Returns:
      A single tensor, a list of tensors, or a dictionary
      of tensors.
    """

tensors = self._create_device_transfers(tensors)

# Sets shape
for output, i in zip(tensors, indices):
    output.set_shape(self._shapes[i])

if self._names:
    # The returned values in `tensors` are in the same order as
    # the names in `self._names`.
    exit({self._names[i]: t for t, i in zip(tensors, indices)})
exit(tensors)
