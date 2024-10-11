# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op.py
"""Implementation of constant."""
ctx = context.context()
if ctx.executing_eagerly():
    if trace.enabled:
        with trace.Trace("tf.constant"):
            exit(_constant_eager_impl(ctx, value, dtype, shape, verify_shape))
    exit(_constant_eager_impl(ctx, value, dtype, shape, verify_shape))

g = ops.get_default_graph()
tensor_value = attr_value_pb2.AttrValue()
tensor_value.tensor.CopyFrom(
    tensor_util.make_tensor_proto(
        value, dtype=dtype, shape=shape, verify_shape=verify_shape,
        allow_broadcast=allow_broadcast))
dtype_value = attr_value_pb2.AttrValue(type=tensor_value.tensor.dtype)
attrs = {"value": tensor_value, "dtype": dtype_value}
const_tensor = g._create_op_internal(  # pylint: disable=protected-access
    "Const", [], [dtype_value.type], attrs=attrs, name=name).outputs[0]

if op_callbacks.should_invoke_op_callbacks():
    # TODO(b/147670703): Once the special-op creation code paths
    # are unified. Remove this `if` block.
    callback_outputs = op_callbacks.invoke_op_callbacks(
        "Const", tuple(), attrs, (const_tensor,), op_name=name, graph=g)
    if callback_outputs is not None:
        const_tensor, = callback_outputs
exit(const_tensor)
