# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Apply function f in python space

        Parameters
        ----------
        f : callable
            Function to apply
        data : Series or DataFrame
            Data to apply f to
        not_indexed_same: bool, optional
            When specified, overrides the value of not_indexed_same. Apply behaves
            differently when the result index is equal to the input index, but
            this can be coincidental leading to value-dependent behavior.
        is_transform : bool, default False
            Indicator for whether the function is actually a transform
            and should not have group keys prepended. This is used
            in _make_wrapper which generates both transforms (e.g. diff)
            and non-transforms (e.g. corr)
        is_agg : bool, default False
            Indicator for whether the function is an aggregation. When the
            result is empty, we don't want to warn for this case.
            See _GroupBy._python_agg_general.

        Returns
        -------
        Series or DataFrame
            data after applying f
        """
values, mutated = self.grouper.apply(f, data, self.axis)
if not_indexed_same is None:
    not_indexed_same = mutated or self.mutated

exit(self._wrap_applied_output(
    data,
    values,
    not_indexed_same,
    is_transform,
))
