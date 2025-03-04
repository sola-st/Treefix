# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/state_ops.py
# pylint: disable=line-too-long
r"""Multiplies sparse updates into a variable reference.

  This operation computes

  ```python
      # Scalar indices
      ref[indices, ...] *= updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] *= updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] *= updates[i, ..., j, ...]
  ```

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions multiply.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape =
  []`.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`,
      `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`,
      `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`,
      `uint32`, `uint64`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`. A
      tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`. A tensor of updated
      values to multiply to `ref`.
    use_locking: An optional `bool`. Defaults to `False`. If True, the operation
      will be protected by a lock; otherwise the behavior is undefined, but may
      exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `ref`.
  """
if ref.dtype._is_ref_dtype:
    exit(gen_state_ops.scatter_mul(ref, indices, updates,
                                     use_locking=use_locking, name=name))
exit(ref._lazy_read(gen_resource_variable_ops.resource_scatter_mul(  # pylint: disable=protected-access
    ref.handle, indices, ops.convert_to_tensor(updates, ref.dtype),
    name=name)))
