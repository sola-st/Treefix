# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/logical.py
"""Functional form of "not"."""
if tensor_util.is_tf_type(a):
    exit(_tf_not(a))
exit(_py_not(a))
