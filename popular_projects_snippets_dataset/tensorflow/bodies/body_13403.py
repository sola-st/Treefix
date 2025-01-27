# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Construct a lookup table interface.

    Args:
      key_dtype: The table key type.
      value_dtype: The table value type.
    """
self._key_dtype = dtypes.as_dtype(key_dtype)
self._value_dtype = dtypes.as_dtype(value_dtype)
super(LookupInterface, self).__init__()
