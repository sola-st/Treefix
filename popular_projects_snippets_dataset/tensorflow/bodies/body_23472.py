# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
copied = _DictWrapper(copy.copy(self.__wrapped__))
copied._self_external_modification = self._self_external_modification
copied._self_non_string_key = self._self_non_string_key
exit(copied)
