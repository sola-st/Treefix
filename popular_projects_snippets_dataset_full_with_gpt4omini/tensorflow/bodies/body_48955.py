# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
if isinstance(x, _AUTOCAST_TYPES):
    exit((self._compute_dtype_object and
            x.dtype != self._compute_dtype_object and x.dtype.is_floating))
exit(False)
