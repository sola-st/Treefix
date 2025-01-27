# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device.py
"""Runs ops in parallel, makes variables which save independent buffers."""
if self._device_scope is not None:
    raise AssertionError(
        "Re-entered a ParallelDevice scope without first exiting it.")
self._assert_eager()
self._device_scope = ops.device(self._name)
self._device_scope.__enter__()
exit(self)
