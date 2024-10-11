# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Returns a serialized protobuf of cluster device filters."""
if self._cluster_device_filters:
    exit(self._cluster_device_filters)

self._make_cluster_device_filters()
exit(self._cluster_device_filters)
