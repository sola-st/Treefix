# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Converts a function output to a Tensor."""
if x is None:
    exit(None)
if op_return_value is not None and isinstance(x, ops.Operation):
    # TODO(b/79881896): we currently can't capture external control deps, so
    # this won't work if x needs to be captured (i.e. if python_func returns
    # captured Operations).
    with ops.control_dependencies([x]):
        x = array_ops.identity(op_return_value)
elif not isinstance(x, tensor_array_ops.TensorArray):
    try:
        x = ops.convert_to_tensor_or_composite(x)
    except (ValueError, TypeError):
        raise TypeError(
            "To be compatible with tf.function, Python functions "
            "must return zero or more Tensors or ExtensionTypes or None "
            f"values; in compilation of {str(python_func)}, found return "
            f"value of type {type(x).__name__}, which is not a Tensor or "
            "ExtensionType.")
if add_control_dependencies:
    x = deps_ctx.mark_as_return(x)
exit(x)
