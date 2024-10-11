# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Creates a non-initialized `HashTable` object.

    Creates a table, the type of its keys and values are specified by the
    initializer.
    Before using the table you will have to initialize it. After initialization
    the table will be immutable.

    Args:
      initializer: The table initializer to use. See `HashTable` kernel for
        supported key and value types.
      default_value: The value to use if a key is missing in the table.
      name: A name for the operation (optional).
      experimental_is_anonymous: Whether to use anonymous mode for the
        table (default is False). In anonymous mode, the table
        resource can only be accessed via a resource handle. It can't
        be looked up by a name. When all resource handles pointing to
        that resource are gone, the resource will be deleted
        automatically.

    Returns:
      A `HashTable` object.
    """
self._initializer = initializer
self._default_value = default_value
self._is_anonymous = experimental_is_anonymous
if not self._is_anonymous:
    self._shared_name = self._initializer._shared_name  # pylint: disable=protected-access
    if not self._shared_name:
        # Force using a shared name so that StaticHashTable resources can be
        # shared across different kernels. If no "shared_name" is set and
        # "use_node_name_sharing" is False, then each kernel gets its own local
        # resource.
        self._shared_name = "hash_table_%s" % (str(uuid.uuid4()),)
self._name = name or "hash_table"
self._table_name = None
super(StaticHashTable, self).__init__(default_value, initializer)
self._value_shape = self._default_value.get_shape()
