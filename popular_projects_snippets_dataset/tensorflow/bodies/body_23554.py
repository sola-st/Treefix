# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
"""Returns the resource handle associated with this Resource."""
if self._resource_handle is None:
    with ops.device(self._resource_device):
        self._resource_handle = self._create_resource()
exit(self._resource_handle)
