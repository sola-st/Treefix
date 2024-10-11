# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Make a copy of this object. Names, dtype, levels and codes can be
        passed and will be set on new copy.

        Parameters
        ----------
        names : sequence, optional
        deep : bool, default False
        name : Label
            Kept for compatibility with 1-dimensional Index. Should not be used.

        Returns
        -------
        MultiIndex

        Notes
        -----
        In most cases, there should be no functional difference from using
        ``deep``, but if ``deep`` is passed it will attempt to deepcopy.
        This could be potentially expensive on large MultiIndex objects.
        """
names = self._validate_names(name=name, names=names, deep=deep)
keep_id = not deep
levels, codes = None, None

if deep:
    from copy import deepcopy

    levels = deepcopy(self.levels)
    codes = deepcopy(self.codes)

levels = levels if levels is not None else self.levels
codes = codes if codes is not None else self.codes

new_index = type(self)(
    levels=levels,
    codes=codes,
    sortorder=self.sortorder,
    names=names,
    verify_integrity=False,
)
new_index._cache = self._cache.copy()
new_index._cache.pop("levels", None)  # GH32669
if keep_id:
    new_index._id = self._id
exit(new_index)
