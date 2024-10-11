# Extracted from ./data/repos/pandas/pandas/core/interchange/column.py
"""
        See `self.dtype` for details.
        """
# Note: 'c' (complex) not handled yet (not in array spec v1).
#       'b', 'B' (bytes), 'S', 'a', (old-style string) 'V' (void) not handled
#       datetime and timedelta both map to datetime (is timedelta handled?)

kind = _NP_KINDS.get(dtype.kind, None)
if kind is None:
    # Not a NumPy dtype. Check if it's a categorical maybe
    raise ValueError(f"Data type {dtype} not supported by interchange protocol")

exit((kind, dtype.itemsize * 8, dtype_to_arrow_c_fmt(dtype), dtype.byteorder))
