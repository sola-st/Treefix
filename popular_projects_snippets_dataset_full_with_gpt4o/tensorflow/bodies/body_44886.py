# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/lang/special_functions.py
"""Casts a value to be staged at the same level as another."""
if tensor_util.is_tf_type(like_value):
    exit(constant_op.constant(value))
exit(value)
