# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
filter_override = registry_lookup(filter_registry, iterable)
if filter_override is not None:
    exit(filter_override(function, iterable))
exit(_py_filter(function, iterable))
