# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
with ops.device(
    colocate_with.device), distribute_lib.UpdateContext(colocate_with):
    result = fn(*args, **kwargs)
    if group:
        exit(result)
    else:
        exit(nest.map_structure(self._local_results, result))
