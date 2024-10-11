# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
dtype = getattr(_autocast_dtype, 'dtype', None)
exit(dtype or self._variable.dtype)
