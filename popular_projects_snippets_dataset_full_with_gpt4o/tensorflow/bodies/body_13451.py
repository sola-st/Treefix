# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Construct a `StaticVocabularyTable` object.

    Args:
      initializer: A `TableInitializerBase` object that contains the data used
        to initialize the table. If None, then we only use out-of-vocab buckets.
      num_oov_buckets: Number of buckets to use for out-of-vocabulary keys. Must
        be greater than zero. If out-of-vocab buckets are not required, use
        `StaticHashTable` instead.
      lookup_key_dtype: Data type of keys passed to `lookup`. Defaults to
        `initializer.key_dtype` if `initializer` is specified, otherwise
        `tf.string`. Must be string or integer, and must be castable to
        `initializer.key_dtype`.
      name: A name for the operation (optional).
      experimental_is_anonymous: Whether to use anonymous mode for the
        table (default is False). In anonymous mode, the table
        resource can only be accessed via a resource handle. It can't
        be looked up by a name. When all resource handles pointing to
        that resource are gone, the resource will be deleted
        automatically.

    Raises:
      ValueError: when `num_oov_buckets` is not positive.
      TypeError: when lookup_key_dtype or initializer.key_dtype are not
        integer or string. Also when initializer.value_dtype != int64.
    """
if num_oov_buckets <= 0:
    raise ValueError("`num_oov_buckets` must be > 0; use StaticHashTable.")
# If a name ends with a '/' it is a "name scope", remove all trailing '/'
# characters to use as table name.
if name:
    name = name.rstrip("/")
if initializer:
    if lookup_key_dtype is None:
        lookup_key_dtype = initializer.key_dtype
    supported_table_key_dtypes = (dtypes.int64, dtypes.string)
    if initializer.key_dtype not in supported_table_key_dtypes:
        raise TypeError("Invalid `key_dtype`, expected one of %s, but got %s." %
                        (supported_table_key_dtypes, initializer.key_dtype))
    if initializer.key_dtype.is_integer != lookup_key_dtype.is_integer:
        raise TypeError(
            "Invalid `key_dtype`, expected %s but got %s." %
            ("integer" if lookup_key_dtype.is_integer else "non-integer",
             initializer.key_dtype))
    if initializer.value_dtype != dtypes.int64:
        raise TypeError("Invalid `value_dtype`, expected %s but got %s." %
                        (dtypes.int64, initializer.value_dtype))
    if isinstance(initializer, trackable_base.Trackable):
        self._initializer = self._track_trackable(initializer, "_initializer")
    self._table = HashTable(
        initializer,
        default_value=-1,
        experimental_is_anonymous=experimental_is_anonymous)
    name = name or self._table.name
else:
    lookup_key_dtype = dtypes.string
    self._table = None
    name = name or "hash_bucket"
if (not lookup_key_dtype.is_integer) and (dtypes.string !=
                                          lookup_key_dtype):
    raise TypeError("Invalid `key_dtype`, expected integer or string, got "
                    f"{lookup_key_dtype}")
self._num_oov_buckets = num_oov_buckets

self._table_name = None
if name is not None:
    self._table_name = name.split("/")[-1]
super(StaticVocabularyTable, self).__init__(lookup_key_dtype, dtypes.int64)
