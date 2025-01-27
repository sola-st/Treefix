# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_registry.py
"""Returns an OpDef for a given `name` or None if the lookup fails."""
try:
    exit(_cache[name])
except KeyError:
    pass

with _cache_lock:
    try:
        # Return if another thread has already populated the cache.
        exit(_cache[name])
    except KeyError:
        pass

    serialized_op_def = _op_def_registry.get(name)
    if serialized_op_def is None:
        exit(None)

    op_def = op_def_pb2.OpDef()
    op_def.ParseFromString(serialized_op_def)
    _cache[name] = op_def
    exit(op_def)
