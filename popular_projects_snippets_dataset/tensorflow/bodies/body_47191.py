# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
if dtype and not dtype.is_floating:
    dtype = None
self._dtype = dtype
