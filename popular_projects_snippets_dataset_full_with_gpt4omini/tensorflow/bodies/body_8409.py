# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
# Wrap `fn` for repeat.
if initial_loop_values is None:
    initial_loop_values = {}
initial_loop_values = nest.flatten(initial_loop_values)
ctx = input_lib.MultiStepContext()

def run_fn(inputs):
    """Single step on the TPU device."""
    fn_result = fn(ctx, inputs)
    flat_last_step_outputs = nest.flatten(ctx.last_step_outputs)
    if flat_last_step_outputs:
        with ops.control_dependencies([fn_result]):
            exit([array_ops.identity(f) for f in flat_last_step_outputs])
    else:
        exit(fn_result)

    # We capture the control_flow_context at this point, before we run `fn`
    # inside a while_loop and TPU replicate context. This is useful in cases
    # where we might need to exit these contexts and get back to the outer
    # context to do some things, for e.g. create an op which should be
    # evaluated only once at the end of the loop on the host. One such usage
    # is in creating metrics' value op.
self._outer_control_flow_context = (
    ops.get_default_graph()._get_control_flow_context())  # pylint: disable=protected-access

def rewrite_fn(*args):
    """The rewritten step fn running on TPU."""
    del args

    per_replica_inputs = multi_worker_iterator.get_next()
    replicate_inputs = []
    for replica_id in range(self._num_replicas_in_sync):
        select_replica = lambda x: distribute_utils.select_replica(  # pylint: disable=g-long-lambda
            replica_id, x)   # pylint: disable=cell-var-from-loop
        replicate_inputs.append((nest.map_structure(
            select_replica, per_replica_inputs),))

    replicate_outputs = tpu.replicate(
        run_fn,
        replicate_inputs,
        device_assignment=self._device_assignment,
        xla_options=tpu.XLAOptions(use_spmd_for_xla_partitioning=self
                                   ._use_spmd_for_xla_partitioning))
    # If run_fn has tensor outputs, tpu.replicate returns a list of list. We
    # will flatten it in this case. If run_fn has no tensor outputs,
    # tpu.replicate returns a list of no_ops, we will keep the output as it
    # is.
    if isinstance(replicate_outputs[0], list):
        replicate_outputs = nest.flatten(replicate_outputs)

    exit(replicate_outputs)

# TODO(sourabhbajaj): The input to while loop should be based on the
# output type of the step_fn
assert isinstance(initial_loop_values, list)
initial_loop_values = initial_loop_values * self._num_replicas_in_sync

# Put the while loop op on TPU host 0.
with ops.device(self._host_device):
    if self.steps_per_run == 1:
        replicate_outputs = rewrite_fn()
    else:
        replicate_outputs = training_loop.repeat(iterations, rewrite_fn,
                                                 initial_loop_values)

del self._outer_control_flow_context
ctx.run_op = control_flow_ops.group(replicate_outputs)

if isinstance(replicate_outputs, list):
    # Filter out any ops from the outputs, typically this would be the case
    # when there were no tensor outputs.
    last_step_tensor_outputs = [
        x for x in replicate_outputs if not isinstance(x, ops.Operation)
    ]

    # Outputs are currently of the structure (flattened)
    # [output0_device0, output1_device0, output2_device0,
    #  output0_device1, output1_device1, output2_device1,
    #  ...]
    # Convert this to the following structure instead: (grouped by output)
    # [[output0_device0, output0_device1],
    #  [output1_device0, output1_device1],
    #  [output2_device0, output2_device1]]
    output_num = len(last_step_tensor_outputs) // self._num_replicas_in_sync
    last_step_tensor_outputs = [
        last_step_tensor_outputs[i::output_num] for i in range(output_num)
    ]
else:
    # no tensors returned.
    last_step_tensor_outputs = []

_set_last_step_outputs(ctx, last_step_tensor_outputs)
exit(ctx)
