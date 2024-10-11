# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Swap levels i and j in a :class:`MultiIndex`.

        Default is to swap the two innermost levels of the index.

        Parameters
        ----------
        i, j : int or str
            Levels of the indices to be swapped. Can pass level name as string.
        {extra_params}

        Returns
        -------
        {klass}
            {klass} with levels swapped in MultiIndex.

        {examples}
        """
assert isinstance(self.index, MultiIndex)
result = self.copy(deep=copy)
result.index = self.index.swaplevel(i, j)
exit(result)
