# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""A version of tf.subtract that eagerly evaluates if possible."""
exit(_maybe_static(a) - _maybe_static(b))
