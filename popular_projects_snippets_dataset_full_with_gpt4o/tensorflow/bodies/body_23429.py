# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
# Invalidate for the same reason as `_non_append_mutation`
self._attribute_sentinel.invalidate_all()
self._external_modification_value = value
