# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Traces gradient functions and records them in the SaveableView."""
functions = list(graph._functions.values())  # pylint: disable=protected-access
func_graph_map = {f.graph: f for f in functions if hasattr(f, "graph")}
seen_op_types = set()

for fn in functions:
    for op_type, op in _iterate_op_types(fn):
        if op_type in seen_op_types:
            continue
        seen_op_types.add(op_type)

        try:
            custom_gradient = ops.gradient_registry.lookup(op_type)
        except LookupError:
            continue

        try:
            grad_fn = (
                def_function.function(custom_gradient).get_concrete_function(
                    None, *op.inputs))
        except Exception as exc:
            traceback.print_exc()
            raise ValueError(
                "Error when tracing gradients for SavedModel.\n\n"
                "Check the error log to see the error that was raised when "
                "converting a gradient function to a concrete function. You may "
                "need to update the custom gradient, or disable saving gradients "
                "with the option "
                "tf.saved_model.SaveOptions(experimental_custom_gradients=False)"
                f".\n\tProblematic op name: {op.name}\n\tGradient inputs: "
                f"{op.inputs}") from exc

        # The gradient function will capture all intermediate values. These
        # captures be serialized so that they can be re-bound to the function when
        # loading.
        bad_captures = []
        for capture in grad_fn.captured_inputs:
            if capture.dtype in _UNCOPIABLE_DTYPES:
                continue
            # Tries to find the outermost capture in case the tensor is a constant
            # or not actually captured in the current function (this could happen if
            # the function is a while loop body, in which case the captured input
            # is not the internal captured tensor).
            outer_fn, outer_capture = _get_outer_most_capture(
                fn, capture, func_graph_map)
            if outer_fn is None or isinstance(outer_capture, ops.EagerTensor):
                if outer_capture not in saveable_view.captured_tensor_node_ids:
                    raise ValueError(f"Found invalid capture {outer_capture} when "
                                     "saving custom gradients.")
                saveable_view.captured_tensor_node_ids[capture] = (
                    saveable_view.captured_tensor_node_ids[outer_capture])
            elif outer_capture.graph is outer_fn.graph:
                capture_name = outer_capture.name
                # It's possible for EagerDefinedFunctions to save different names for
                # input tensors when serialized to FunctionDef (all non-alphanumeric
                # characters are converted to '_').
                if isinstance(outer_fn, defun._EagerDefinedFunction):  # pylint:disable=protected-access
                    try:
                        arg_index = outer_fn.graph.inputs.index(outer_capture)
                        capture_name = outer_fn.signature.input_arg[arg_index].name + ":0"
                    except ValueError:
                        pass

                node = _CapturedTensor(capture_name, outer_fn.name)
                saveable_view.add_capture_and_node(capture, node)
            else:
                bad_captures.append(capture.name)
        if not bad_captures:
            grad_fn.add_to_graph(graph)
        else:
            raise ValueError(
                f"Cannot save custom gradient {op_type} called in function {fn} "
                "because SavedModel is unable to serialize the captured "
                f"inputs: {bad_captures}")

        saveable_view.gradient_functions.append(grad_fn)
        func_graph_map[grad_fn.graph] = grad_fn

        grad_def = function_pb2.RegisteredGradient()
        grad_def.gradient_func = grad_fn.name
        grad_def.registered_op_type = op_type
        saveable_view.gradient_defs.append(grad_def)
