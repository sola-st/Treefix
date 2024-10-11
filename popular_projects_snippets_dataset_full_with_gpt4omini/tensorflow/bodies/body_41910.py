# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Executes the wrapped function.

    Args:
      args: a list of Tensors or Variables. Arguments from the Python function
        should be filtered before calling this method: objects aside from
        Tensors, CompositeTensors, and Variables are ignored. Any
        CompositeTensors other than ResourceVariables should be expanded before
        calling this method.
      captured_inputs: the captured inputs that are also part of the input args
        to the actual execution. By default, it should be self._captured_inputs.
      cancellation_manager: (Optional.) A `CancellationManager` that can be
        used to cancel function invocation.

    Returns:
      The result of applying the TF function to `args`.

    Raises:
      ValueError: If `args` contains anything other than Tensors or Variables.
    """
ctx = context.context()
executing_eagerly = ctx.executing_eagerly()

# Copy saveable status of function's graph to current FuncGraph.
default_graph = ops.get_default_graph()
if default_graph.building_function and not self._func_graph.saveable:
    default_graph.mark_as_unsaveable(self._func_graph.saving_errors)

if (tape.could_possibly_record() or
    hasattr(default_graph, "watch_variable")):
    for v in self._func_graph.variables:
        resource_variable_ops.variable_accessed(v)

tensor_inputs = []
variables_used = set([])
for i, arg in enumerate(args):
    if isinstance(arg, resource_variable_ops.BaseResourceVariable):
        # We can pass a variable more than once, and in this case we need to
        # pass its handle only once.
        if id(arg.handle) in variables_used:
            continue
        resource_variable_ops.variable_accessed(arg)
        tensor_inputs.append(arg.handle)
        variables_used.add(id(arg.handle))
    elif isinstance(arg, ops.Tensor):
        tensor_inputs.append(arg)
    else:
        raise ValueError(f"{i:d}-th input {arg} must be a Tensor, got "
                         f"{type(arg)} when calling {self._func_graph.name}.")

if not executing_eagerly:
    for i, tensor_input in enumerate(tensor_inputs):
        # Can not compare shapes in these cases
        # TODO(b/216506654): Consider moving this check elsewhere and making it
        # work for all types (e.g. by including shape for Variables).
        if (tensor_input.dtype == dtypes.resource or
            tensor_input.dtype == dtypes.variant):
            continue

        # If we're graph building, shape inference is on. We check for input
        # compatibility up front to avoid hard to debug incompatibilities
        # later.
        graph_input_shape = tensor_shape.TensorShape(
            self._func_graph.inputs[i].shape)
        if not graph_input_shape.is_compatible_with(tensor_input.shape):
            raise ValueError(
                f"Tensor {tensor_input} is not compatible with the shape this "
                f"function was traced with. Expected shape "
                f"{self._func_graph.inputs[i].shape}, but got shape "
                f"{tensor_input.shape}.\n\nIf you called get_concrete_function, "
                f"you may need to pass a tf.TensorSpec(..., shape=...) with a "
                f"less specific shape, having None on axes which can vary.")

args = tensor_inputs + captured_inputs
possible_gradient_type = gradients_util.PossibleTapeGradientTypes(args)
if (possible_gradient_type == gradients_util.POSSIBLE_GRADIENT_TYPES_NONE
    and executing_eagerly):
    # No tape is watching; skip to running the function.
    exit(self._build_call_outputs(self._inference_function.call(
        ctx, args, cancellation_manager=cancellation_manager)))
forward_backward = self._select_forward_and_backward_functions(
    args,
    possible_gradient_type,
    executing_eagerly)
forward_function, args_with_tangents = forward_backward.forward()
if executing_eagerly:
    flat_outputs = forward_function.call(
        ctx, args_with_tangents, cancellation_manager=cancellation_manager)
else:
    with default_graph._override_gradient_function(  # pylint: disable=protected-access
        {"PartitionedCall": self._get_gradient_function(),
         "StatefulPartitionedCall": self._get_gradient_function()}):
        flat_outputs = forward_function.call(ctx, args_with_tangents)
forward_backward.record(flat_outputs)
exit(self._build_call_outputs(flat_outputs))
