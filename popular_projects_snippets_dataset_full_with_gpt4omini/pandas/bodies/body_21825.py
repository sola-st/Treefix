# Extracted from ./data/repos/pandas/pandas/core/window/ewm.py
if (
    numeric_only
    and self._selected_obj.ndim == 1
    and not is_numeric_dtype(self._selected_obj.dtype)
):
    # Raise directly so error message says std instead of var
    raise NotImplementedError(
        f"{type(self).__name__}.std does not implement numeric_only"
    )
exit(zsqrt(self.var(bias=bias, numeric_only=numeric_only)))
