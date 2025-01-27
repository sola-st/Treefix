# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Construct a `IdTableWithHashBuckets` object.

    Args:
      table: Table that maps `tf.string` or `tf.int64` keys to `tf.int64` ids.
      num_oov_buckets: Number of buckets to use for out-of-vocabulary keys.
      hasher_spec: A `HasherSpec` to specify the hash function to use for
        assignation of out-of-vocabulary buckets  (optional).
      name: A name for the operation (optional).
      key_dtype: Data type of keys passed to `lookup`. Defaults to
        `table.key_dtype` if `table` is specified, otherwise `tf.string`. Must
        be string or integer, and must be castable to `table.key_dtype`.

    Raises:
      ValueError: when `table` in None and `num_oov_buckets` is not positive.
      TypeError: when `hasher_spec` is invalid.
    """
# If a name ends with a '/' it is a "name scope", remove all trailing '/'
# characters to use as table name.
if name:
    name = name.rstrip("/")
if table:
    if key_dtype is None:
        key_dtype = table.key_dtype
    supported_table_key_dtypes = (dtypes.int64, dtypes.string)
    if table.key_dtype not in supported_table_key_dtypes:
        raise TypeError("Invalid `key_dtype`, expected one of "
                        f"{supported_table_key_dtypes}, received {key_dtype}.")
    if table.key_dtype.is_integer != key_dtype.is_integer:
        raise TypeError("Invalid `key dtype`, expected %s but got %s." %
                        ("integer" if key_dtype.is_integer else "non-integer",
                         table.key_dtype))
    if table.value_dtype != dtypes.int64:
        raise TypeError("Invalid `value_dtype`: expected int64 but got %s." %
                        (table.value_dtype))
    self._table = table
    name = name or self._table.name
else:
    if num_oov_buckets <= 0:
        raise ValueError("`oov_buckets` must be > 0 if no `table` is supplied.")
    key_dtype = dtypes.string if key_dtype is None else key_dtype
    self._table = None
    name = name or "hash_bucket"
if (not key_dtype.is_integer) and (dtypes.string != key_dtype):
    raise TypeError("Invalid `key_dtype`, expected integer or string, got "
                    f"{key_dtype}.")
self._num_oov_buckets = num_oov_buckets

if not isinstance(hasher_spec, HasherSpec):
    raise TypeError("`hasher_spec` must be of type HasherSpec, got "
                    f"{type(hasher_spec)}.")
self._hasher_spec = hasher_spec
if name:
    self._table_name = name.split("/")[-1]
else:
    self._table_name = None
super(IdTableWithHashBuckets, self).__init__(key_dtype, dtypes.int64)
