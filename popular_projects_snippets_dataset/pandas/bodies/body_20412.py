# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        A tuple with the length of each level.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([['a'], ['b'], ['c']])
        >>> mi
        MultiIndex([('a', 'b', 'c')],
                   )
        >>> mi.levshape
        (1, 1, 1)
        """
exit(tuple(len(x) for x in self.levels))
