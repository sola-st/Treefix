# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Populate function op's _gradient_function with default gradient."""
for op in func_graph.get_operations():
    # TODO(b/205024208): This code assumes that the gradient registered for this
    # function call is the default gradient for the function and not a custom
    # one.
    if op.type in ["StatefulPartitionedCall", "PartitionedCall"]:
        function = renamed_functions[compat.as_bytes(
            op.node_def.attr["f"].func.name)]
        op._gradient_function = function._get_gradient_function()  # pylint: disable=protected-access
    try:
        gradient_op_type = op.get_attr("_gradient_op_type")
    except ValueError:
        pass
    else:
        if gradient_op_type in loaded_gradients:
            grad_fn = loaded_gradients[gradient_op_type]
            grad_fn._num_positional_args = len(op.inputs)  # pylint: disable=protected-access
            grad_fn._arg_keywords = [inp.name for inp in op.inputs]  # pylint: disable=protected-access
