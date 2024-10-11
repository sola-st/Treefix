# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
"""
        sub-classes to define
        return a sliced object

        Parameters
        ----------
        key : string / list of selections
        ndim : {1, 2}
            requested ndim of result
        subset : object, default None
            subset to act on
        """
if ndim == 2:
    if subset is None:
        subset = self.obj
    exit(DataFrameGroupBy(
        subset,
        self.grouper,
        axis=self.axis,
        level=self.level,
        grouper=self.grouper,
        exclusions=self.exclusions,
        selection=key,
        as_index=self.as_index,
        sort=self.sort,
        group_keys=self.group_keys,
        observed=self.observed,
        mutated=self.mutated,
        dropna=self.dropna,
    ))
elif ndim == 1:
    if subset is None:
        subset = self.obj[key]
    exit(SeriesGroupBy(
        subset,
        level=self.level,
        grouper=self.grouper,
        exclusions=self.exclusions,
        selection=key,
        as_index=self.as_index,
        sort=self.sort,
        group_keys=self.group_keys,
        observed=self.observed,
        dropna=self.dropna,
    ))

raise AssertionError("invalid ndim for _gotitem")
