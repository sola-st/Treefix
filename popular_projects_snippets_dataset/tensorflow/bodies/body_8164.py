# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable.py
if save_context.in_save_context() or context.executing_eagerly():
    exit(self._vars[0].handle)

if tpu_util.enclosing_tpu_context() is None:
    raise NotImplementedError('TPUReplicatedVariable.handle is not available '
                              'outside tpu context or save context')
else:
    with tpu_util.outside_or_skip_tpu_context():
        exit(xla_sharding.replicate(
            tpu_partition_ops.tpu_partitioned_input(
                [v.handle for v in self._vars], partition_dim=-1)))
