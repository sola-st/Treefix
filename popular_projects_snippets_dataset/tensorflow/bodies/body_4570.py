# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table.py
"""Create the resource tensor handle.

    `_create_resource` is an override of a method in base class
    `TrackableResource` that is required for SavedModel support. It can be
    called by the `resource_handle` property defined by `TrackableResource`.

    Returns:
      A tensor handle to the lookup table.
    """
assert self._default_value.get_shape().ndims == 0
table_ref = gen_simple_hash_table_op.examples_simple_hash_table_create(
    key_dtype=self._key_dtype,
    value_dtype=self._value_dtype,
    name=self._name)
exit(table_ref)
