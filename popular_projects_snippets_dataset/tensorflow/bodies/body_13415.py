# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Looks up `keys` in a table, outputs the corresponding values.

    The `default_value` is used for keys not present in the table.

    Args:
      keys: Keys to look up. May be either a `SparseTensor` or dense `Tensor`.
      name: A name for the operation (optional).

    Returns:
      A `SparseTensor` if keys are sparse, a `RaggedTensor` if keys are ragged,
      otherwise a dense `Tensor`.

    Raises:
      TypeError: when `keys` or `default_value` doesn't match the table data
        types.
    """
key_tensor = keys
if isinstance(keys,
              (sparse_tensor.SparseTensor, ragged_tensor.RaggedTensor)):
    key_tensor = keys.values

if keys.dtype.base_dtype != self._key_dtype:
    raise TypeError(f"Dtype of argument `keys` must be {self._key_dtype}, "
                    f"received: {keys.dtype}")

with ops.name_scope(
    name, "%s_Lookup" % self.name,
    (self.resource_handle, key_tensor, self._default_value)):
    values = gen_lookup_ops.lookup_table_find_v2(self.resource_handle,
                                                 key_tensor,
                                                 self._default_value)

values.set_shape(key_tensor.get_shape())
if isinstance(keys, sparse_tensor.SparseTensor):
    exit(sparse_tensor.SparseTensor(keys.indices, values, keys.dense_shape))
elif isinstance(keys, ragged_tensor.RaggedTensor):
    exit(keys.with_values(values))
else:
    exit(values)
