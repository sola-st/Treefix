# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
del colocate_with
with ops.device(self._device), distribute_lib.UpdateContext(self._device):
    result = fn(*args, **kwargs)
    if group:
        exit(result)
    else:
        exit(nest.map_structure(self._local_results, result))
