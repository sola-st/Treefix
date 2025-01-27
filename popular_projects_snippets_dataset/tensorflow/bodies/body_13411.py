# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Construct a table object from a table reference.

    If requires a table initializer object (subclass of `TableInitializerBase`).
    It provides the table key and value types, as well as the op to initialize
    the table. The caller is responsible to execute the initialization op.

    Args:
      default_value: The value to use if a key is missing in the table.
      initializer: The table initializer to use.
    """
super(InitializableLookupTableBase, self).__init__(initializer.key_dtype,
                                                   initializer.value_dtype)
self._default_value = ops.convert_to_tensor(
    default_value, dtype=self._value_dtype)
self._default_value.get_shape().merge_with(tensor_shape.TensorShape([]))
if isinstance(initializer, trackable_base.Trackable):
    self._initializer = self._track_trackable(initializer, "_initializer")
with ops.init_scope():
    self._resource_handle = self._create_resource()
if (not context.executing_eagerly() and
    ops.get_default_graph()._get_control_flow_context() is not None):  # pylint: disable=protected-access
    with ops.init_scope():
        self._init_op = self._initialize()
else:
    self._init_op = self._initialize()
