# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
"""
        Validates that we have a valid ordered parameter. If
        it is not a boolean, a TypeError will be raised.

        Parameters
        ----------
        ordered : object
            The parameter to be verified.

        Raises
        ------
        TypeError
            If 'ordered' is not a boolean.
        """
if not is_bool(ordered):
    raise TypeError("'ordered' must either be 'True' or 'False'")
