# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
copied = super().__deepcopy__(memo)
copied._non_append_mutation = self._non_append_mutation
copied._external_modification = self._external_modification
exit(copied)
