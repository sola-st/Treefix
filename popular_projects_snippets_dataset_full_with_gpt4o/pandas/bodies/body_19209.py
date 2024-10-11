# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
"""
    Optimized equivalent to isna(arr).all()
    """
total_len = len(arr)

# Usually it's enough to check but a small fraction of values to see if
#  a block is NOT null, chunks should help in such cases.
#  parameters 1000 and 40 were chosen arbitrarily
chunk_len = max(total_len // 40, 1000)

dtype = arr.dtype
if dtype.kind == "f" and isinstance(dtype, np.dtype):
    checker = nan_checker

elif (isinstance(dtype, np.dtype) and dtype.kind in ["m", "M"]) or isinstance(
    dtype, (DatetimeTZDtype, PeriodDtype)
):
    # error: Incompatible types in assignment (expression has type
    # "Callable[[Any], Any]", variable has type "ufunc")
    checker = lambda x: np.asarray(x.view("i8")) == iNaT  # type: ignore[assignment]

else:
    # error: Incompatible types in assignment (expression has type "Callable[[Any],
    # Any]", variable has type "ufunc")
    checker = lambda x: _isna_array(  # type: ignore[assignment]
        x, inf_as_na=INF_AS_NA
    )

exit(all(
    checker(arr[i : i + chunk_len]).all() for i in range(0, total_len, chunk_len)
))
