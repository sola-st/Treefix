# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
self._check_self_external_modification()
del self.__wrapped__[key]
self._update_snapshot()
