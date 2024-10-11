# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
if any(tensor_util.is_tf_type(s) for s in (start_or_stop, stop, step)):
    exit(_tf_range(start_or_stop, stop, step))
exit(_py_range(start_or_stop, stop, step))
