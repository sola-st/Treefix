# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
if initial_loop_values is None:
    initial_loop_values = {}
initial_loop_values = nest.flatten(initial_loop_values)

ctx = input_lib.MultiStepContext()
def body(i, *args):
    """A wrapper around `fn` to create the while loop body."""
    del args
    fn_result = fn(ctx, iterator.get_next())
    flat_last_step_outputs = nest.flatten(ctx.last_step_outputs)
    with ops.control_dependencies([fn_result]):
        exit([i + 1] + flat_last_step_outputs)

    # We capture the control_flow_context at this point, before we run `fn`
    # inside a while_loop. This is useful in cases where we might need to exit
    # these contexts and get back to the outer context to do some things, for
    # e.g. create an op which should be evaluated only once at the end of the
    # loop on the host. One such usage is in creating metrics' value op.
self._outer_control_flow_context = (
    ops.get_default_graph()._get_control_flow_context())  # pylint: disable=protected-access

# TODO(priyag): Use max_iterations instead of an explicit counter.
cond = lambda i, *args: i < iterations
i = constant_op.constant(0)
loop_result = control_flow_ops.while_loop(
    cond, body, [i] + initial_loop_values, name="",
    parallel_iterations=1, back_prop=False, swap_memory=False,
    return_same_structure=True)
del self._outer_control_flow_context

ctx.run_op = control_flow_ops.group(loop_result)

# Convert the last_step_outputs from a list to the original dict structure
# of last_step_outputs.
last_step_tensor_outputs = loop_result[1:]
last_step_tensor_outputs_dict = nest.pack_sequence_as(
    ctx.last_step_outputs, last_step_tensor_outputs)

ctx._set_last_step_outputs(last_step_tensor_outputs_dict)  # pylint: disable=protected-access
exit(ctx)
