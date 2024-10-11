# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Asserts tensors are all valid types (see `_valid_dtypes`).

    Args:
      tensors: Tensors to check.

    Raises:
      ValueError: If any tensor is not a valid type.
    """
valid_dtypes = self._valid_dtypes()
for t in tensors:
    dtype = t.dtype.base_dtype
    if dtype not in valid_dtypes:
        raise ValueError(
            "Invalid type %r for %s, expected: %s." % (
                dtype, t.name, [v for v in valid_dtypes]))
