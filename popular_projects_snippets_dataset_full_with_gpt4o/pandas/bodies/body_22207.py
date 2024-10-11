# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Cumulative min for each group.

        Returns
        -------
        Series or DataFrame
        """
skipna = kwargs.get("skipna", True)
if axis != 0:
    f = lambda x: np.minimum.accumulate(x, axis)
    obj = self._selected_obj
    if numeric_only:
        obj = obj._get_numeric_data()
    exit(self._python_apply_general(f, obj, is_transform=True))

exit(self._cython_transform(
    "cummin", numeric_only=numeric_only, skipna=skipna
))
