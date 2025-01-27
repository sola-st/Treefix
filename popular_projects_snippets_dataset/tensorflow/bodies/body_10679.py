# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Validate and convert `vals` to a list of `Tensor`s.

    The `vals` argument can be a Tensor, a list or tuple of tensors, or a
    dictionary with tensor values.

    If `vals` is a list, then the appropriate indices associated with the
    values must be provided.

    If it is a dictionary, the staging area must have been constructed with a
    `names` attribute and the dictionary keys must match the staging area names.
    `indices` will be inferred from the dictionary keys.
    If the staging area was constructed with a `names` attribute, `vals` must
    be a dictionary.

    Checks that the dtype and shape of each value matches that
    of the staging area.

    Args:
      vals: A tensor, a list or tuple of tensors, or a dictionary.

    Returns:
      A (tensors, indices) tuple where `tensors` is a list of `Tensor` objects
      and `indices` is a list of indices associated with the tensors.

    Raises:
      ValueError: If `vals` or `indices` is invalid.
    """
if isinstance(vals, dict):
    if not self._names:
        raise ValueError(
            "Staging areas must have names to enqueue a dictionary")
    if not set(vals.keys()).issubset(self._names):
        raise ValueError("Keys in dictionary to put do not match names "
                         f"of staging area. Dictionary: {sorted(vals.keys())}"
                         f"Queue: {sorted(self._names)}")
    # The order of values in `self._names` indicates the order in which the
    # tensors in the dictionary `vals` must be listed.
    vals, indices, _ = zip(*[(vals[k], i, k)
                             for i, k in enumerate(self._names)
                             if k in vals])
else:
    if self._names:
        raise ValueError("You must enqueue a dictionary in a staging area "
                         "with names")

    if indices is None:
        raise ValueError("Indices must be supplied when inserting a list "
                         "of tensors")

    if len(indices) != len(vals):
        raise ValueError(f"Number of indices {len(indices)} doesn't match "
                         f"number of values {len(vals)}")

    if not isinstance(vals, (list, tuple)):
        vals = [vals]
        indices = [0]

    # Sanity check number of values
if not len(vals) <= len(self._dtypes):
    raise ValueError(f"Unexpected number of inputs {len(vals)} vs "
                     f"{len(self._dtypes)}")

tensors = []

for val, i in zip(vals, indices):
    dtype, shape = self._dtypes[i], self._shapes[i]
    # Check dtype
    if val.dtype != dtype:
        raise ValueError(f"Datatypes do not match. "
                         f"Received val.dtype {str(val.dtype)} and "
                         f"dtype {str(dtype)}")
    # Check shape
    val.get_shape().assert_is_compatible_with(shape)

    tensors.append(
        ops.convert_to_tensor(val, dtype=dtype, name="component_%d" % i))

exit((tensors, indices))
