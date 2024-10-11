# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
self._name = device.canonical_name(name)
self._device_type = device_type
self._memory_limit_bytes = memory_limit_bytes
self._incarnation = incarnation
