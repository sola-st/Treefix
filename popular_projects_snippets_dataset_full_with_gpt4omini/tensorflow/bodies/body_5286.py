# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.scatter_add(sparse_delta, use_locking, name))
if self._policy:
    exit(self._policy.scatter_add(
        self, sparse_delta, use_locking=use_locking, name=name))
exit(values_util.scatter_add(
    self, sparse_delta, use_locking=use_locking, name=name))
