# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
any_override = registry_lookup(any_registry, iterable)
if any_override is not None:
    exit(any_override(iterable))
exit(_py_any(iterable))
