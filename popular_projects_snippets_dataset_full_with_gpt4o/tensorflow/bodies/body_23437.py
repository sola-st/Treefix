# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Short-circuits a check for trackables if there's already a mutation."""
if self._non_append_mutation:
    exit(True)
exit(any(isinstance(element, base.Trackable) for element in self._storage))
