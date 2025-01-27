# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
if not (np.isscalar(value) or isinstance(value, (list, tuple, np.ndarray))):
    raise TypeError(
        f"Invalid type for initial value: {type(value).__name__}. Expected "
        "Python scalar, list or tuple of values, or numpy.ndarray.")
self.value = value
