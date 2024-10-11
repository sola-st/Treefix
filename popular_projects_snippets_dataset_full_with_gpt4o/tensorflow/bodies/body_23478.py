# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Acknowledges tracked changes to the wrapped dict."""
self._attribute_sentinel.invalidate_all()
if self._dirty:
    exit()
self._self_last_wrapped_dict_snapshot = dict(self)
