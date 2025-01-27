# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns a list of local device specs represented as strings."""
exit([d.to_string() for d in self._local_devices])
