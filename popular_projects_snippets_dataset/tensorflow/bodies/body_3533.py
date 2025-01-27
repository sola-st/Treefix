# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform.py
"""Copies over any custom_gradients defined within the original Graph."""
seen_ops = set()
for gradient_op_type, op in _ops_with_custom_gradients(
    replicated_graph.get_operations()):
    # Soft-cache processed ops so we do not repeat the computation.
    if gradient_op_type in seen_ops:
        continue
    seen_ops.add(gradient_op_type)

    # Lookup the custom_gradient implementation if it exists. Currently all
    # custom_gradients are stored as python functions in a gradient_registry.
    # The gradient_registry returns a LookupError when a lookup fails.
    try:
        custom_gradient = ops.gradient_registry.lookup(gradient_op_type)
    except LookupError:
        continue

    # Convert the custom_gradient to a `ConcreteFunction`. This is done so we
    # can replicate the custom gradient and update any python captures.
    try:
        grad_fn = def_function.function(custom_gradient).get_concrete_function(
            None, *op.inputs)
    except Exception:  # pylint: disable=broad-except
        # TODO(xjun): Figure out why tracing of custom_gradient will fail.
        tf_logging.exception(
            f"Error when tracing gradients for {replicated_graph}.")
        continue

    # Re-bind all captures to values within the replicated graph.
    remapped_captures = []
    for capture in grad_fn.captured_inputs:
        outer_graph, outer_capture = _get_outer_most_capture(
            original_graph, capture)

        # We only need to re-bind captures originating from the `original_graph`.
        if outer_graph is not original_graph:
            continue

        if outer_capture.graph is not outer_graph:
            raise ValueError(
                f"Cannot replicate graph: {original_graph}. It utilizes a "
                f"`tf.custom_gradient` for op: {op} which has a "
                f"non-replicable capture: {capture}. Consider re-factoring your "
                f"custom_gradient to avoid the capture.")

        remapped_captures.append(
            replicated_graph.get_tensor_by_name(outer_capture.name))
    saved_model_utils.restore_captures(grad_fn, remapped_captures)
    new_gradient_op_type = custom_gradient_lib.generate_name()
    op._set_attr(  # pylint: disable=protected-access
        "_gradient_op_type",
        attr_value_pb2.AttrValue(s=compat.as_bytes(new_gradient_op_type)))
    ops.RegisterGradient(new_gradient_op_type)(_gen_gradient_func(grad_fn))
