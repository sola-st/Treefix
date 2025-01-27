# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return Index without NA/NaN values.

        Parameters
        ----------
        how : {'any', 'all'}, default 'any'
            If the Index is a MultiIndex, drop the value when any or all levels
            are NaN.

        Returns
        -------
        Index
        """
if how not in ("any", "all"):
    raise ValueError(f"invalid how option: {how}")

if self.hasnans:
    res_values = self._values[~self._isnan]
    exit(type(self)._simple_new(res_values, name=self.name))
exit(self._view())
