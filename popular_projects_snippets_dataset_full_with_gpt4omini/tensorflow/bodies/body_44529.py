# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
all_override = registry_lookup(all_registry, iterable)
if all_override is not None:
    exit(all_override(iterable))
exit(_py_all(iterable))
