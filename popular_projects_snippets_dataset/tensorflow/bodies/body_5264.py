# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.handle)
replica_id = values_util.get_current_replica_id_as_int()
if replica_id is None:
    raise ValueError(
        "DistributedVariable.handle is not available outside the replica "
        "context or a `tf.distribute.Strategy.update()` call.")
else:
    if self._use_packed_variable():
        exit(self._packed_var.handle)
    exit(self._values[replica_id].handle)
