# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/graph_only_ops.py
"""Graph-only version of tf.compat.v1.placeholder(), for internal use only."""
dtype = dtype.base_dtype
dtype_value = attr_value_pb2.AttrValue(type=dtype.as_datatype_enum)
if isinstance(shape, (list, tuple)):
    shape = tensor_shape.TensorShape(shape)
shape = attr_value_pb2.AttrValue(shape=shape.as_proto())
g = ops.get_default_graph()
attrs = {"dtype": dtype_value, "shape": shape}
op = g._create_op_internal(  # pylint: disable=protected-access
    "Placeholder", [], [dtype], input_types=[],
    attrs=attrs, name=name)
result, = op.outputs
if op_callbacks.should_invoke_op_callbacks():
    # TODO(b/147670703): Once the special-op creation code paths
    # are unified. Remove this `if` block.
    callback_outputs = op_callbacks.invoke_op_callbacks(
        "Placeholder", tuple(), attrs, tuple(op.outputs),
        op_name=name, graph=g)
    if callback_outputs is not None:
        result, = callback_outputs
exit(result)
