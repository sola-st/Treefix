# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
if tensor_util.is_tf_type(x):
    exit(_tf_int(x, base))
exit(_py_int(x, base))
