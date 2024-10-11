# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
distribute_lib.require_replica_context(self)
ds = self._strategy
replica_id = tensor_util.constant_value(self.replica_id_in_sync_group)

if replica_id is None:  # Non-constant `Tensor` inside `tpu.replicate`.
    # TODO(cjfj): Return other devices when model parallelism is supported.
    exit((tpu.core(0),))
else:
    exit((ds.extended.worker_devices[replica_id],))
