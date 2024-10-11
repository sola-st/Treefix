# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Creates an empty `MutableHashTable` object.

    Creates a table, the type of its keys and values are specified by key_dtype
    and value_dtype, respectively.

    Args:
      key_dtype: the type of the key tensors.
      value_dtype: the type of the value tensors.
      default_value: The value to use if a key is missing in the table.
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
      A `MutableHashTable` object.

    Raises:
      ValueError: If checkpoint is True and no name was specified.
    """
self._default_value = ops.convert_to_tensor(
    default_value, dtype=value_dtype)
self._value_shape = self._default_value.get_shape()
self._checkpoint = checkpoint
self._key_dtype = key_dtype
self._value_dtype = value_dtype
self._name = name
self._is_anonymous = experimental_is_anonymous
if not self._is_anonymous:
    self._shared_name = None
    if context.executing_eagerly():
        # TODO(allenl): This will leak memory due to kernel caching by
        # the shared_name attribute value (but is better than the
        # alternative of sharing everything by default when executing
        # eagerly; hopefully creating tables in a loop is uncommon).
        self._shared_name = "table_%d" % (ops.uid(),)
super(MutableHashTable, self).__init__(key_dtype, value_dtype)
self._resource_handle = self._create_resource()
if checkpoint:
    saveable = MutableHashTable._Saveable(self, name)
    if not context.executing_eagerly():
        ops.add_to_collection(ops.GraphKeys.SAVEABLE_OBJECTS, saveable)
