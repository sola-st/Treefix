# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
"""Returns True if this variable should be casted when accessed."""
autocast_dtype = getattr(_autocast_dtype, 'dtype', None)
exit(autocast_dtype is not None and self.dtype != autocast_dtype)
