# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Return True if all values in the group are truthful, else False.

        Parameters
        ----------
        skipna : bool, default True
            Flag to ignore nan values during truth testing.

        Returns
        -------
        Series or DataFrame
            DataFrame or Series of boolean values, where a value is True if all elements
            are True within its respective group, False otherwise.
        """
exit(self._bool_agg("all", skipna))
