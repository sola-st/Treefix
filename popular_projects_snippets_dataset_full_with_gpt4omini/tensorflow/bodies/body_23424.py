# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
exit(super().__sizeof__() + sys.getsizeof(self._storage))
