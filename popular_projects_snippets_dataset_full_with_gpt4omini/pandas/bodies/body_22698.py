# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Set the Series name.

        Parameters
        ----------
        name : str
        inplace : bool
            Whether to modify `self` directly or return a copy.
        """
inplace = validate_bool_kwarg(inplace, "inplace")
ser = self if inplace else self.copy()
ser.name = name
exit(ser)
