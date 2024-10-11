# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
exit(self._id_in_cluster * len(self.worker_devices) + replica_id)
