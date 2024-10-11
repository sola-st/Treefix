# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
super(OneDeviceExtended, self).__init__(container_strategy)
self._device = device_util.resolve(device)
self._input_device = device_util.get_host_for_device(self._device)
