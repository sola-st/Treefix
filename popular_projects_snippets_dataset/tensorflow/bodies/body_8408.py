# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
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
