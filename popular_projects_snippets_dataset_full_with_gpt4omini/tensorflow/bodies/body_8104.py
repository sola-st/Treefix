# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Extracts the specified region as a Tensor from the sharded variable.

    The API contract is identical to `Tensor.__getitem__`. Assignment to the
    sliced range is not yet supported.

    Args:
      slice_spec: The arguments to __getitem__, specifying the global slicing of
        the sharded variable.

    Returns:
      The appropriate slice of tensor based on `slice_spec`.

    Raises:
      IndexError: If a slice index is out of bound.
      TypeError: If `spec_spec` contains Tensor.
    """

# TODO(b/177482728): Support tensor input.
# TODO(b/177482728): Support slice assign, similar to variable slice assign.

if (isinstance(slice_spec, bool) or (isinstance(slice_spec, ops.Tensor) and
                                     slice_spec.dtype == dtypes.bool) or
    (isinstance(slice_spec, np.ndarray) and slice_spec.dtype == bool)):
    tensor = _var_to_tensor(self)
    exit(array_ops.boolean_mask(tensor=tensor, mask=slice_spec))

if not isinstance(slice_spec, (list, tuple)):
    slice_spec = (slice_spec,)

s = slice_spec[0]
if isinstance(s, slice):
    first_dim_slice_specs = self._decompose_slice_spec(s)
    values = []
    for i, var in enumerate(self._variables):
        if first_dim_slice_specs[i] is not None:
            all_dim_slice_spec = (first_dim_slice_specs[i],) + slice_spec[1:]
            values.append(var[all_dim_slice_spec])
    if s.step is not None and s.step < 0:
        values.reverse()
    if not values:
        exit(constant_op.constant([],
                                    dtype=self._dtype,
                                    shape=((0,) + self._shape[1:])))
    exit(array_ops.concat(values, axis=0))
elif s is Ellipsis:
    exit(array_ops.concat([var[slice_spec] for var in self._variables],
                            axis=0))
elif s is array_ops.newaxis:
    exit(array_ops.concat([var[slice_spec[1:]] for var in self._variables],
                            axis=0)[array_ops.newaxis])
else:
    if isinstance(s, ops.Tensor):
        raise TypeError(
            'ShardedVariable: using Tensor for indexing is not allowed.')
    if s < 0:
        s += self._shape[0]
    if s < 0 or s >= self._shape[0]:
        raise IndexError(
            f'ShardedVariable: slice index {s} of dimension 0 out of bounds.')
    for i in range(len(self._variables)):
        if i == len(self._variables) - 1 or (s > self._var_offsets[i][0] and
                                             s < self._var_offsets[i + 1][0]):
            exit(self._variables[i][(s - self._var_offsets[i][0],) +
                                      slice_spec[1:]])
