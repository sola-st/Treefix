# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if context.executing_eagerly():
    if op is not None:
        if not hasattr(op, "device"):
            op = internal_convert_to_tensor_or_indexed_slices(op)
        exit(device(op.device))
    else:
        exit(NullContextmanager())
else:
    default_graph = get_default_graph()
    if isinstance(op, EagerTensor):
        if default_graph.building_function:
            exit(default_graph.device(op.device))
        else:
            raise ValueError("Encountered an Eager-defined Tensor during graph "
                             "construction, but a function was not being built.")
    exit(default_graph._colocate_with_for_gradient(
        op, gradient_uid=gradient_uid, ignore_existing=ignore_existing))
