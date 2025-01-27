# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
if isinstance(value_rank, int):
    output_shape = list(value_shape)
    output_shape[axis] *= self.num_replicas_in_sync
else:
    output_shape = array_ops.where_v2(
        math_ops.equal(math_ops.range(value_rank), axis),
        value_shape * context.num_replicas_in_sync,
        value_shape)
exit(output_shape)
