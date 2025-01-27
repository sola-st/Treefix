# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Return the value to return from a dequeue op.

    If the queue has names, return a dictionary with the
    names as keys.  Otherwise return either a single tensor
    or a list of tensors depending on the length of `tensors`.

    Args:
      tensors: List of tensors from the dequeue op.

    Returns:
      A single tensor, a list of tensors, or a dictionary
      of tensors.
    """
if self._names:
    # The returned values in `tensors` are in the same order as
    # the names in `self._names`.
    exit({n: tensors[i] for i, n in enumerate(self._names)})
elif len(tensors) == 1:
    exit(tensors[0])
else:
    exit(tensors)
