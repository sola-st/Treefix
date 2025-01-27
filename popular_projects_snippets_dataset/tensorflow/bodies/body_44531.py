# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
if tensor_util.is_tf_type(iterable):
    exit(_tf_sorted(iterable, key, reverse))
exit(_py_sorted(iterable, key, reverse))
