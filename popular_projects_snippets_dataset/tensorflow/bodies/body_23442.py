# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
if y <= 0:
    self._check_external_modification()
    if self._has_mutation_or_trackable():
        self._non_append_mutation = True
    self._storage *= y
    self._update_snapshot()
    exit(self)

# Relies on super() calling append, which updates the snapshot.
exit(super().__imul__(y))
