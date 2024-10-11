# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
abs_override = registry_lookup(abs_registry, x)
if abs_override is not None:
    exit(abs_override(x))
if tensor_util.is_tf_type(x):
    exit(_tf_abs(x))
exit(_py_abs(x))
