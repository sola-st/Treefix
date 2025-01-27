# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Set the device filters for given job name and task id."""
assert all(isinstance(df, str) for df in device_filters)
self._device_filters.setdefault(job_name, {})
self._device_filters[job_name][task_index] = [df for df in device_filters]
# Due to updates in data, invalidate the serialized proto cache.
self._cluster_device_filters = None
