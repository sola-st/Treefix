# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
self._prev_dtype = getattr(_autocast_dtype, 'dtype', None)
_autocast_dtype.dtype = self._dtype
