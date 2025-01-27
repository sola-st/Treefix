# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
"""Graph-only version of tf.compat.v1.placeholder(), for internal use only."""
dtype = self.dtype.base_dtype
shape = self.shape
dtype_value = attr_value_pb2.AttrValue(type=dtype.as_datatype_enum)
if isinstance(shape, (list, tuple)):
    shape = tensor_shape.TensorShape(shape)
shape = attr_value_pb2.AttrValue(shape=shape.as_proto())
attrs = {"dtype": dtype_value, "shape": shape}
try:
    op = graph._create_op_internal(  # pylint: disable=protected-access
        "Placeholder", [], [dtype], input_types=[],
        attrs=attrs, name=name)
except ValueError as e:
    # TODO(b/262413656) Sometimes parameter names are not valid op names, in
    # which case an unnamed placeholder is created instead. Update this logic
    # to sanitize the name instead of falling back on unnamed placeholders.
    logging.warning(e)
    op = graph._create_op_internal(  # pylint: disable=protected-access
        "Placeholder", [], [dtype], input_types=[], attrs=attrs)
(result,) = op.outputs
if op_callbacks.should_invoke_op_callbacks():
    # TODO(b/147670703): Once the special-op creation code paths
    # are unified. Remove this `if` block.
    callback_outputs = op_callbacks.invoke_op_callbacks(
        "Placeholder", tuple(), attrs, tuple(op.outputs),
        op_name=name, graph=graph)
    if callback_outputs is not None:
        (result,) = callback_outputs
exit(result)
