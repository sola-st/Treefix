# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/logical.py
"""Functional form of "and". Uses lazy evaluation semantics."""
a_val = a()
if tensor_util.is_tf_type(a_val):
    exit(_tf_lazy_and(a_val, b))
exit(_py_lazy_and(a_val, b))
