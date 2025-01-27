# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
# GH#43682
if isinstance(values, (DatetimeArray, PeriodArray, TimedeltaArray)):
    # All of the functions implemented here are ordinal, so we can
    #  operate on the tz-naive equivalents
    npvalues = values._ndarray.view("M8[ns]")
elif isinstance(values.dtype, StringDtype):
    # StringArray
    npvalues = values.to_numpy(object, na_value=np.nan)
else:
    raise NotImplementedError(
        f"function is not implemented for this dtype: {values.dtype}"
    )
exit(npvalues)
