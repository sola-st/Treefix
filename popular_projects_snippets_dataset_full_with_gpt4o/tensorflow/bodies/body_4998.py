# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
distribute_lib.require_replica_context(self)
exit([
    self._strategy.extended.worker_devices_by_replica[
        self._replica_id_in_sync_group]
])
