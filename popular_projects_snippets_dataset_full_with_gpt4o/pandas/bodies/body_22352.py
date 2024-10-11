# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
    Utility frequency conversion method for Series/DataFrame.

    See :meth:`pandas.NDFrame.asfreq` for full documentation.
    """
if isinstance(obj.index, PeriodIndex):
    if method is not None:
        raise NotImplementedError("'method' argument is not supported")

    if how is None:
        how = "E"

    new_obj = obj.copy()
    new_obj.index = obj.index.asfreq(freq, how=how)

elif len(obj.index) == 0:
    new_obj = obj.copy()

    new_obj.index = _asfreq_compat(obj.index, freq)
else:
    dti = date_range(obj.index.min(), obj.index.max(), freq=freq)
    dti.name = obj.index.name
    new_obj = obj.reindex(dti, method=method, fill_value=fill_value)
    if normalize:
        new_obj.index = new_obj.index.normalize()

exit(new_obj)
