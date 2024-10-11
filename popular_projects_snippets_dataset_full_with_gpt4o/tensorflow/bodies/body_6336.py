# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
# TODO(josh11b): Figure out what we should be passing to UpdateContext()
# once that value is used for something.
with UpdateContext(colocate_with):
    result = fn(*args, **kwargs)
    if should_group:
        exit(result)
    else:
        exit(nest.map_structure(self._local_results, result))
