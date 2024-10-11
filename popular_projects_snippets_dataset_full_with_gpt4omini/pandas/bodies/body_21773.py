# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        Return a scalar result of performing the reduction operation.

        Parameters
        ----------
        name : str
            Name of the function, supported values are:
            { any, all, min, max, sum, mean, median, prod,
            std, var, sem, kurt, skew }.
        skipna : bool, default True
            If True, skip NaN values.
        **kwargs
            Additional keyword arguments passed to the reduction function.
            Currently, `ddof` is the only supported kwarg.

        Returns
        -------
        scalar

        Raises
        ------
        TypeError : subclass does not define reductions
        """
meth = getattr(self, name, None)
if meth is None:
    raise TypeError(
        f"'{type(self).__name__}' with dtype {self.dtype} "
        f"does not support reduction '{name}'"
    )
exit(meth(skipna=skipna, **kwargs))
