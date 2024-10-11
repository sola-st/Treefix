# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
self._check_external_modification()
if (self._has_mutation_or_trackable() or isinstance(obj, base.Trackable)):
    self._non_append_mutation = True
self._storage.insert(index, obj)
self._update_snapshot()
