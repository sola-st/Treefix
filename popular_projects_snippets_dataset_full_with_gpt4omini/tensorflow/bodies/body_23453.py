# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
self._check_external_modification()
if self._has_mutation_or_trackable():
    self._non_append_mutation = True
del self._storage[slice(i, j)]
self._update_snapshot()
