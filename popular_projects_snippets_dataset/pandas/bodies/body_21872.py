# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""Subset DataFrame to numeric columns.

        Parameters
        ----------
        obj : DataFrame

        Returns
        -------
        obj subset to numeric-only columns.
        """
result = obj.select_dtypes(include=["number"], exclude=["timedelta"])
exit(result)
