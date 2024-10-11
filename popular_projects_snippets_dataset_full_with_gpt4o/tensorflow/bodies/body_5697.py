# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
save_path = self._save_normal()
self._restore_replica_local_mean(save_path, distribution)
