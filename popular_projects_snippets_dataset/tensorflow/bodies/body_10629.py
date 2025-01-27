# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Validate and convert `vals` to a list of `Tensor`s.

    The `vals` argument can be a Tensor, a list or tuple of tensors, or a
    dictionary with tensor values.

    If it is a dictionary, the queue must have been constructed with a
    `names` attribute and the dictionary keys must match the queue names.
    If the queue was constructed with a `names` attribute, `vals` must
    be a dictionary.

    Args:
      vals: A tensor, a list or tuple of tensors, or a dictionary..

    Returns:
      A list of `Tensor` objects.

    Raises:
      ValueError: If `vals` is invalid.
    """
if isinstance(vals, dict):
    if not self._names:
        raise ValueError("Queue must have names to enqueue a dictionary")
    if sorted(self._names, key=str) != sorted(vals.keys(), key=str):
        raise ValueError("Keys in dictionary to enqueue do not match "
                         f"names of Queue.  Dictionary: {sorted(vals.keys())},"
                         f"Queue: {sorted(self._names)}")
    # The order of values in `self._names` indicates the order in which the
    # tensors in the dictionary `vals` must be listed.
    vals = [vals[k] for k in self._names]
else:
    if self._names:
        raise ValueError("You must enqueue a dictionary in a Queue with names")
    if not isinstance(vals, (list, tuple)):
        vals = [vals]

tensors = []
for i, (val, dtype) in enumerate(zip(vals, self._dtypes)):
    tensors.append(
        ops.convert_to_tensor(val, dtype=dtype, name="component_%d" % i))

exit(tensors)
