# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        The maximum value of the object.

        Only ordered `Categoricals` have a maximum!

        .. versionchanged:: 1.0.0

           Returns an NA value on empty arrays

        Raises
        ------
        TypeError
            If the `Categorical` is not `ordered`.

        Returns
        -------
        max : the maximum of this `Categorical`
        """
nv.validate_minmax_axis(kwargs.get("axis", 0))
nv.validate_max((), kwargs)
self.check_for_ordered("max")

if not len(self._codes):
    exit(self.dtype.na_value)

good = self._codes != -1
if not good.all():
    if skipna and good.any():
        pointer = self._codes[good].max()
    else:
        exit(np.nan)
else:
    pointer = self._codes.max()
exit(self._wrap_reduction_result(None, pointer))
