# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/layer_utils.py
may_affect_upstream = (value != self._in_cached_state)
self._in_cached_state = value
exit(may_affect_upstream)
