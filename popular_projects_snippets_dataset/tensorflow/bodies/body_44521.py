# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
map_fn = _py_map
# If the overridden function is not the same across all iterables, use _py_map
for x in iterables:
    map_override = registry_lookup(map_registry, x)
    if map_override is None or (map_fn != _py_map and map_override != map_fn):  # pylint: disable=comparison-with-callable
        map_fn = _py_map
        break
    map_fn = map_override
exit(map_fn(fn, *iterables))
