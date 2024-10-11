# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
"""
        Shared logic for __truediv__, __floordiv__, and their reversed versions
        with timedelta64-dtype ndarray other.
        """
# Let numpy handle it
result = op(self._ndarray, np.asarray(other))

if (is_integer_dtype(other.dtype) or is_float_dtype(other.dtype)) and op in [
    operator.truediv,
    operator.floordiv,
]:
    exit(type(self)._simple_new(result, dtype=result.dtype))

if op in [operator.floordiv, roperator.rfloordiv]:
    mask = self.isna() | isna(other)
    if mask.any():
        result = result.astype(np.float64)
        np.putmask(result, mask, np.nan)

exit(result)
