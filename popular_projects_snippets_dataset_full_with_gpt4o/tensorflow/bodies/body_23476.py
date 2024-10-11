# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Check if there has already been a mutation which prevents saving."""
exit((self._self_external_modification
        or self._self_non_string_key))
