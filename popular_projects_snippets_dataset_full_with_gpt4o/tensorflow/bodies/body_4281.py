# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns True if a Mesh contains only remote devices."""
exit(not self._local_device_ids and self._global_device_ids.size > 0)
