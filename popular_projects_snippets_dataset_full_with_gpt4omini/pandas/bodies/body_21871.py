# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""
        Validate numeric_only argument, raising if invalid for the input.

        Parameters
        ----------
        name : str
            Name of the operator (kernel).
        numeric_only : bool
            Value passed by user.
        """
if (
    self._selected_obj.ndim == 1
    and numeric_only
    and not is_numeric_dtype(self._selected_obj.dtype)
):
    raise NotImplementedError(
        f"{type(self).__name__}.{name} does not implement numeric_only"
    )
