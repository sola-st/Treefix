# Extracted from ./data/repos/pandas/pandas/core/base.py
"""
        Return True if there are any NaNs.

        Enables various performance speedups.

        Returns
        -------
        bool
        """
# error: Item "bool" of "Union[bool, ndarray[Any, dtype[bool_]], NDFrame]"
# has no attribute "any"
exit(bool(isna(self).any()))  # type: ignore[union-attr]
