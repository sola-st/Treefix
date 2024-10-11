# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Calls this function with `args` as inputs.

    `ConcreteFunction` execution respects device annotations only if the
    function won't be compiled with xla.

    Args:
      ctx: a Context object
      args: a list of arguments to supply this function with.
      cancellation_manager: a `CancellationManager` object that can be used to
        cancel function execution.

    Returns:
      The outputs of the function call.

    Raises:
      ValueError: if the number of arguments is incorrect.
      FunctionAlreadyGarbageCollectedError: if the function is no longer
        available to be called because it has been garbage collected.
    """
if len(args) != len(self.signature.input_arg):
    raise ValueError(
        f"Signature specifies {len(list(self.signature.input_arg))} "
        f"arguments, got: {len(args)}.")

function_call_options = ctx.function_call_options
if function_call_options.config_proto_serialized is None:
    config = function_utils.get_disabled_rewriter_config()
else:
    config = function_call_options.config_proto_serialized
executor_type = function_call_options.executor_type or ""

executing_eagerly = ctx.executing_eagerly()
attrs = ("executor_type", executor_type, "config_proto", config)
if executing_eagerly:
    with _InterpolateFunctionError(self):
        if cancellation_manager is None:
            outputs = execute.execute(
                str(self.signature.name),
                num_outputs=self._num_outputs,
                inputs=args,
                attrs=attrs,
                ctx=ctx)
        else:
            outputs = execute.execute_with_cancellation(
                str(self.signature.name),
                num_outputs=self._num_outputs,
                inputs=args,
                attrs=attrs,
                ctx=ctx,
                cancellation_manager=cancellation_manager)
      # Replace empty list with None
    outputs = outputs or None
else:
    # TODO(akshayka): Either remove this if the FunctionLibraryRuntime
    # creates `PartitionedCallOp` kernels by default, or remove the previous
    # branch if a TPU kernel is registered for `PartitionedCall`.
    with _InterpolateFunctionError(self):
        with ops.control_dependencies(self._control_captures):
            # The caller must use record_operation to record this operation in the
            # eager case, so we enforce the same requirement for the non-eager
            # case by explicitly pausing recording. We don't have a gradient
            # registered for PartitionedCall, so recording this operation confuses
            # forwardprop code (GradientTape manages to ignore it).
            with tape.stop_recording():
                outputs = functional_ops.partitioned_call(
                    args=args,
                    f=self,
                    tout=self._output_types,
                    executing_eagerly=executing_eagerly,
                    config=config,
                    executor_type=executor_type)

for i, func_graph_output in enumerate(self._func_graph_outputs):
    handle_data_util.copy_handle_data(func_graph_output, outputs[i])
if executing_eagerly:
    exit(outputs)
else:
    # TODO(b/128924522): This additional set_shape should not be
    # necessary. ShapeRefiner likely needs to inspect handle_data. Remove this
    # once that's done.
    for i, shape in enumerate(self._output_shapes):
        outputs[i].set_shape(shape)
    exit(outputs)
