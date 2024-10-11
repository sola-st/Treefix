# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
"""For implementing `Trackable`."""
new_obj = copy.copy(self)
# pylint: disable=protected-access
with ops.device(self._resource_device):
    new_resource = new_obj._create_resource()
new_obj._resource_handle = new_resource
# pylint: enable=protected-access
object_map[self] = new_obj
tensor_map[self.resource_handle] = new_resource
exit([self.resource_handle])
