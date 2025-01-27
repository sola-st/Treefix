# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
if len(key) != 2:
    raise ValueError(f"`key` must have size 2, received {len(key)}")

if not isinstance(key[0], compat_util.integral_types) or not isinstance(
    key[1], compat_util.integral_types):
    raise TypeError("Invalid key %s. Must be unsigned integer values." % key)

exit(super(cls, StrongHashSpec).__new__(cls, "stronghash", key))
