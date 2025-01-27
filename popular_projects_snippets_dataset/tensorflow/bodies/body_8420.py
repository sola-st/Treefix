# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
if (isinstance(value, values.DistributedValues) or
    tensor_util.is_tf_type(value)
   ) and tpu_util.enclosing_tpu_context() is not None:
    if reduce_op == reduce_util.ReduceOp.MEAN:
        # TODO(jhseu):  Revisit once we support model-parallelism.
        # scalar_mul maintains the type of value: tensor or IndexedSlices.
        value = math_ops.scalar_mul((1./self._num_replicas_in_sync), value)
    elif reduce_op != reduce_util.ReduceOp.SUM:
        raise NotImplementedError(
            f"`reduce_op`={reduce_op} is not supported. Currently we only "
            "support ReduceOp.SUM and ReduceOp.MEAN in TPUStrategy.")
    exit(tpu_ops.cross_replica_sum(value))

if not isinstance(value, values.DistributedValues):
    # This function handles reducing values that are not PerReplica or
    # Mirrored values. For example, the same value could be present on all
    # replicas in which case `value` would be a single value or value could
    # be 0.
    exit(cross_device_ops_lib.reduce_non_distributed_value(
        reduce_op, value, destinations, self._num_replicas_in_sync))

value_list = value.values
# pylint: disable=protected-access
if isinstance(
    value,
    values.DistributedVariable) and value._packed_variable is not None:
    value_list = tuple(
        value._packed_variable.on_device(d)
        for d in value._packed_variable.devices)
# pylint: enable=protected-access

# Currently XLA op by op mode has a limit for the number of inputs for a
# single op, thus we break one `add_n` op into a group of `add_n` ops to
# work around the constraint.
# TODO(cjfj): Detect when it is possible to use `cross_replica_sum`.
if len(value.values) <= _XLA_OP_BY_OP_INPUTS_LIMIT:
    output = math_ops.add_n(value_list)
else:
    output = array_ops.zeros_like(value_list[0], dtype=value_list[0].dtype)
    for i in range(0, len(value_list), _XLA_OP_BY_OP_INPUTS_LIMIT):
        output += math_ops.add_n(value_list[i:i + _XLA_OP_BY_OP_INPUTS_LIMIT])

if reduce_op == reduce_util.ReduceOp.MEAN:
    output *= (1. / len(value_list))

output = self._broadcast_output(destinations, output)
exit(output)
