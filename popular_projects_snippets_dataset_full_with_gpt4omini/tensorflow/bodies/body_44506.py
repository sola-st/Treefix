# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
if any(tensor_util.is_tf_type(s) for s in args):
    exit(_tf_min(*args, **kwargs))
exit(_py_min(*args, **kwargs))
