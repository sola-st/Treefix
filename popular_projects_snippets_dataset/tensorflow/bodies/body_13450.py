# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Looks up `keys` in the table, outputs the corresponding values.

    It assigns out-of-vocabulary keys to buckets based in their hashes.

    Args:
      keys: Keys to look up. May be either a `SparseTensor` or dense `Tensor`.
      name: Optional name for the op.

    Returns:
      A `SparseTensor` if keys are sparse, a `RaggedTensor` if keys are ragged,
      otherwise a dense `Tensor`.

    Raises:
      TypeError: when `keys` doesn't match the table key data type.
    """
if keys.dtype.base_dtype != self._key_dtype:
    raise TypeError(f"Dtype of argument `keys` must be {self._key_dtype}, "
                    f"received: {keys.dtype}")
values = keys
if isinstance(keys,
              (sparse_tensor.SparseTensor, ragged_tensor.RaggedTensor)):
    values = keys.values
if self._table and (self._table.key_dtype.base_dtype == dtypes.int64):
    values = math_ops.cast(values, dtypes.int64)

if self._num_oov_buckets == 0:
    ids = self._table.lookup(values, name=name)
else:
    # TODO(yleon): Consider moving this functionality to its own kernel.
    with ops.name_scope(name, "%s_Lookup" % self.name):
        str_to_hash_bucket = self._get_string_to_hash_bucket_fn(
            self._hasher_spec)
        buckets = str_to_hash_bucket(
            _as_string(values),
            num_buckets=self._num_oov_buckets,
            name="hash_bucket")
        if self._table:
            ids = self._table.lookup(values)
            buckets = math_ops.add(buckets, self._table.size())
            is_id_non_default = math_ops.not_equal(ids, self._table.default_value)
            ids = array_ops.where_v2(is_id_non_default, ids, buckets)
        else:
            ids = buckets
if isinstance(keys, sparse_tensor.SparseTensor):
    exit(sparse_tensor.SparseTensor(keys.indices, ids, keys.dense_shape))
elif isinstance(keys, ragged_tensor.RaggedTensor):
    exit(keys.with_values(ids))
exit(ids)
