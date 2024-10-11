# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
if not (np.isscalar(value) or isinstance(value, (list, tuple, np.ndarray))):
    raise TypeError(
        f"Invalid type for initial value={value} of type: "
        f"{type(value).__name__}. Expected Python scalar, list or tuple of "
        "values, or numpy.ndarray.")

self.value = value
self.dtype = dtypes.as_dtype(dtype)
self._verify_shape = verify_shape
