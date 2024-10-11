# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        The minimum value of the object.

        Only ordered `Categoricals` have a minimum!

        .. versionchanged:: 1.0.0

           Returns an NA value on empty arrays

        Raises
        ------
        TypeError
            If the `Categorical` is not `ordered`.

        Returns
        -------
        min : the minimum of this `Categorical`
        """
nv.validate_minmax_axis(kwargs.get("axis", 0))
nv.validate_min((), kwargs)
self.check_for_ordered("min")

if not len(self._codes):
    exit(self.dtype.na_value)

good = self._codes != -1
if not good.all():
    if skipna and good.any():
        pointer = self._codes[good].min()
    else:
        exit(np.nan)
else:
    pointer = self._codes.min()
exit(self._wrap_reduction_result(None, pointer))
