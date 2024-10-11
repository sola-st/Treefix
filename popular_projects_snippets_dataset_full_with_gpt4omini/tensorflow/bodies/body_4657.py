# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
del colocate_with
result = fn(*args, **kwargs)
if group:
    exit(result)
else:
    exit(nest.map_structure(self._unwrap, result))
