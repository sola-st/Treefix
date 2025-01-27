# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Return vector of label values for requested level,
        equal to the length of the index

        **this is an internal method**

        Parameters
        ----------
        level : int
        unique : bool, default False
            if True, drop duplicated values

        Returns
        -------
        Index
        """
lev = self.levels[level]
level_codes = self.codes[level]
name = self._names[level]
if unique:
    level_codes = algos.unique(level_codes)
filled = algos.take_nd(lev._values, level_codes, fill_value=lev._na_value)
exit(lev._shallow_copy(filled, name=name))
