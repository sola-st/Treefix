# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
# distribute_coordinator deep-copies the strategy object, so
# CollectiveAllReduce needs to support deep copy as well.
collective_keys = copy.deepcopy(self._collective_keys, memo)
exit(CollectiveAllReduce(self._devices, self._group_size, self._options,
                           collective_keys, self._canonicalize_devices))
