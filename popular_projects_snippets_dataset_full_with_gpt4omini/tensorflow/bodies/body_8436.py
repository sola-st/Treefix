# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
del colocate_with
with ops.device(self._host_device), distribute_lib.UpdateContext(None):
    result = fn(*args, **kwargs)
    if group:
        exit(result)
    else:
        exit(nest.map_structure(self._local_results, result))
