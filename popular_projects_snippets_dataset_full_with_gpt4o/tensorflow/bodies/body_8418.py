# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
if not isinstance(value, values.DistributedValues):
    exit(value)

value_list = list(value.values)
# pylint: disable=protected-access
if isinstance(
    value,
    values.DistributedVariable) and value._packed_variable is not None:
    value_list = list(
        value._packed_variable.on_device(d)
        for d in value._packed_variable.devices)
# pylint: enable=protected-access

# Currently XLA op by op mode has a limit for the number of inputs for a
# single op, thus we break one `add_n` op into a group of `add_n` ops to
# work around the constraint.
if len(value.values) <= _XLA_OP_BY_OP_INPUTS_LIMIT:
    output = array_ops.concat(value_list, axis=axis)
else:
    output = array_ops.concat(
        value_list[:_XLA_OP_BY_OP_INPUTS_LIMIT], axis=axis)
    for i in range(_XLA_OP_BY_OP_INPUTS_LIMIT, len(value_list),
                   _XLA_OP_BY_OP_INPUTS_LIMIT - 1):
        output = array_ops.concat(
            [output] + value_list[i:i + _XLA_OP_BY_OP_INPUTS_LIMIT - 1],
            axis=axis)

output = self._broadcast_output(destinations, output)
exit(output)
