# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
save_path = self._save_replica_local_sum(distribution)
self._restore_replica_local_sum(save_path, distribution)
