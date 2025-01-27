# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/logical.py
"""Functional form of "equal"."""
if tensor_util.is_tf_type(a) or tensor_util.is_tf_type(b):
    exit(_tf_equal(a, b))
exit(_py_equal(a, b))
