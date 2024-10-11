# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Construct a table initializer object.

    Args:
      key_dtype: Type of the table keys.
      value_dtype: Type of the table values.
    """
self._key_dtype = dtypes.as_dtype(key_dtype)
self._value_dtype = dtypes.as_dtype(value_dtype)
