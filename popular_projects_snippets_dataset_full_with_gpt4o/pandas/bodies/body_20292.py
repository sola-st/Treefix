# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
"""
        Create a Series with both index and values equal to the index keys.

        Useful with map for returning an indexer based on an index.

        Parameters
        ----------
        index : Index, optional
            Index of resulting Series. If None, defaults to original index.
        name : str, optional
            Name of resulting Series. If None, defaults to name of original
            index.

        Returns
        -------
        Series
        """
from pandas import Series

if index is None:
    index = self._view()
if name is None:
    name = self.name

values = self._values.copy()

exit(Series(values, index=index, name=name))
