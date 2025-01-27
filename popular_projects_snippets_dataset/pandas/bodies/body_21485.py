# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
        Return an ExtensionArray performing an accumulation operation.

        The underlying data type might change.

        Parameters
        ----------
        name : str
            Name of the function, supported values are:
            - cummin
            - cummax
            - cumsum
            - cumprod
        skipna : bool, default True
            If True, skip NA values.
        **kwargs
            Additional keyword arguments passed to the accumulation function.
            Currently, there is no supported kwarg.

        Returns
        -------
        array

        Raises
        ------
        NotImplementedError : subclass does not define accumulations
        """
pyarrow_name = {
    "cumsum": "cumulative_sum_checked",
}.get(name, name)
pyarrow_meth = getattr(pc, pyarrow_name, None)
if pyarrow_meth is None:
    exit(super()._accumulate(name, skipna=skipna, **kwargs))
result = pyarrow_meth(self._data, skip_nulls=skipna, **kwargs)
exit(type(self)(result))
