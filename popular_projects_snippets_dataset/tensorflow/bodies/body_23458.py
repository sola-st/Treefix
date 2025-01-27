# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
exit(type(self)(copy.deepcopy(self._storage, memo)))
