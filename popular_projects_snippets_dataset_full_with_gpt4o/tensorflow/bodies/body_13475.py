# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Creates an empty `DenseHashTable` object.

    Creates a table, the type of its keys and values are specified by key_dtype
    and value_dtype, respectively.

    Args:
      key_dtype: the type of the key tensors.
      value_dtype: the type of the value tensors.
      default_value: The value to use if a key is missing in the table.
      empty_key: the key to use to represent empty buckets internally. Must not
        be used in insert, remove or lookup operations.
      deleted_key: the key to use to represent deleted buckets internally. Must
        not be used in insert, remove or lookup operations and be different from
        the empty_key.
      initial_num_buckets: the initial number of buckets (optional,
        default to 2^17=131072). Note that the default value is
        relatively large (~1MB), so if you are going to create many
        tables (likely the case when `experimental_is_anonymous` is
        `True`), you should set `initial_num_buckets` to a smaller
        value to reduce memory usage.
      name: A name for the operation (optional).
      checkpoint: if True, the contents of the table are saved to and restored
        from checkpoints. If `shared_name` is empty for a checkpointed table, it
        is shared using the table node name.
      experimental_is_anonymous: Whether to use anonymous mode for the
        table (default is False). In anonymous mode, the table
        resource can only be accessed via a resource handle. It can't
        be looked up by a name. When all resource handles pointing to
        that resource are gone, the resource will be deleted
        automatically.

    Returns:
      A `DenseHashTable` object.

    Raises:
      ValueError: If checkpoint is True and no name was specified.
    """
self._default_value = ops.convert_to_tensor(
    default_value, dtype=value_dtype, name="default_value")
self._key_dtype = key_dtype
self._value_dtype = value_dtype
# TODO(b/201578996): Pick a good default for initial_num_buckets
#   other than 2^17.
self._initial_num_buckets = initial_num_buckets
self._value_shape = self._default_value.get_shape()
self._checkpoint = checkpoint
self._name = name
self._empty_key = empty_key
self._deleted_key = deleted_key
self._is_anonymous = experimental_is_anonymous
if not self._is_anonymous:
    self._shared_name = None
    if context.executing_eagerly():
        # TODO(allenl): This will leak memory due to kernel caching by
        # the shared_name attribute value (but is better than the
        # alternative of sharing everything by default when executing
        # eagerly; hopefully creating tables in a loop is uncommon).
        self._shared_name = "table_%d" % (ops.uid(),)
super(DenseHashTable, self).__init__(key_dtype, value_dtype)
self._resource_handle = self._create_resource()
if checkpoint:
    saveable = DenseHashTable._Saveable(self, name)
    if not context.executing_eagerly():
        ops.add_to_collection(ops.GraphKeys.SAVEABLE_OBJECTS, saveable)
