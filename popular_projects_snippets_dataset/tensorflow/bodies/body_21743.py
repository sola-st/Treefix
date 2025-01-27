# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
# `_device_filters` is a dict mapping job names to job device filters.
# Job device filters further maps task IDs to task device filters.
# Task device filters are a list of strings, each one is a device filter.
self._device_filters = {}

# Serialized protobuf for cluster device filters.
self._cluster_device_filters = None
