# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
if isinstance(value, (ops.Tensor, ops.EagerTensor)):
    value._parent_trackable = weakref.ref(self)  # pylint: disable=protected-access
self._resource_handle_value = value
