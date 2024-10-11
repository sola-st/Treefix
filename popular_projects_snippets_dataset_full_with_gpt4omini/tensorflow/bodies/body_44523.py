# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
next_override = registry_lookup(next_registry, iterator)
if next_override is not None:
    exit(next_override(iterator, default))
exit(next_py(iterator, default))
