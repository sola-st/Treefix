# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Decorator for disabling the layer V2 dtype behavior on a test."""
exit(_set_v2_dtype_behavior(fn, False))
