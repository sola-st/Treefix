# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table.py
"""Creates an empty `SimpleHashTable` object.

    Creates a table, the type of its keys and values are specified by key_dtype
    and value_dtype, respectively.

    Args:
      key_dtype: the type of the key tensors.
      value_dtype: the type of the value tensors.
      default_value: The value to use if a key is missing in the table.
      name: A name for the operation (optional).

    Returns:
      A `SimpleHashTable` object.
    """
super(SimpleHashTable, self).__init__()
self._default_value = tf.convert_to_tensor(default_value, dtype=value_dtype)
self._value_shape = self._default_value.get_shape()
self._key_dtype = key_dtype
self._value_dtype = value_dtype
self._name = name
self._resource_handle = self._create_resource()
