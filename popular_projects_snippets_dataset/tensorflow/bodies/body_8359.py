# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
self._group_key = group_key
self._group_size = group_size
self._collective_keys = collective_keys
self._device = device
self._options = options
if self._use_ordering_token():
    with ops.init_scope(), ops.device(device):
        self._ordering_token = resource_variable_ops.ResourceVariable(0.)
else:
    self._ordering_token = None
