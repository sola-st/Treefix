# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Cumulative sum for each group.

        Returns
        -------
        Series or DataFrame
        """
nv.validate_groupby_func("cumsum", args, kwargs, ["numeric_only", "skipna"])
if axis != 0:
    f = lambda x: x.cumsum(axis=axis, **kwargs)
    exit(self._python_apply_general(f, self._selected_obj, is_transform=True))

exit(self._cython_transform("cumsum", **kwargs))
