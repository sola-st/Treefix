# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
vals = tuple(v.numpy() if tensor_util.is_tf_type(v) else v for v in vals)
# TensorFlow doesn't seem to generate Unicode when passing strings to
# py_func. This causes the print to add a "b'" wrapper to the output,
# which is probably never what you want.
vals = tuple(v.decode('utf-8') if isinstance(v, bytes) else v for v in vals)
print(*vals, **override_kwargs)
