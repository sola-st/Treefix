# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Sets the last step outputs on the given context."""
# Convert replicate_outputs to the original dict structure of
# last_step_outputs.
last_step_tensor_outputs_dict = nest.pack_sequence_as(
    ctx.last_step_outputs, last_step_tensor_outputs)

for name, reduce_op in ctx._last_step_outputs_reduce_ops.items():  # pylint: disable=protected-access
    output = last_step_tensor_outputs_dict[name]
    # For outputs that aren't reduced, return a PerReplica of all values. Else
    # take the first value from the list as each value should be the same.
    if reduce_op is None:
        last_step_tensor_outputs_dict[name] = values.PerReplica(output)
    else:
        # TODO(priyag): Should this return the element or a list with 1 element
        last_step_tensor_outputs_dict[name] = output[0]
ctx._set_last_step_outputs(last_step_tensor_outputs_dict)  # pylint: disable=protected-access
