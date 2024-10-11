# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.scatter_min(sparse_delta, use_locking, name))
exit(self._policy.scatter_min(
    self, sparse_delta, use_locking=use_locking, name=name))
