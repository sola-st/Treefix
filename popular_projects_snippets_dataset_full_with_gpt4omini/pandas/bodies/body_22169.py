# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Compute median of groups, excluding missing values.

        For multiple groupings, the result index will be a MultiIndex

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns.

            .. versionchanged:: 2.0.0

                numeric_only no longer accepts ``None`` and defaults to False.

        Returns
        -------
        Series or DataFrame
            Median of values within each group.
        """
result = self._cython_agg_general(
    "median",
    alt=lambda x: Series(x).median(numeric_only=numeric_only),
    numeric_only=numeric_only,
)
exit(result.__finalize__(self.obj, method="groupby"))
