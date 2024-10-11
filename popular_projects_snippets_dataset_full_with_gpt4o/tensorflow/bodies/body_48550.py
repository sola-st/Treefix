# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Return True if v is a Tensor, array, or is array-like."""
exit((
    hasattr(v, "__getitem__") and
    hasattr(v, "shape") and
    hasattr(v, "dtype") and
    hasattr(v, "__len__")
))
