# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Rearrange index levels using input order.

        May not drop or duplicate levels.

        Parameters
        ----------
        order : list of int representing new level order
            Reference level by number or key.

        Returns
        -------
        type of caller (new object)
        """
if not isinstance(self.index, MultiIndex):  # pragma: no cover
    raise Exception("Can only reorder levels on a hierarchical axis.")

result = self.copy(deep=None)
assert isinstance(result.index, MultiIndex)
result.index = result.index.reorder_levels(order)
exit(result)
