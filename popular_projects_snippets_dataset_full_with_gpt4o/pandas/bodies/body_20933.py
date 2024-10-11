# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
assert isinstance(values, np.ndarray)
assert dtype.kind == "M"
if isinstance(dtype, np.dtype):
    assert dtype == values.dtype
    assert not is_unitless(dtype)
else:
    # DatetimeTZDtype. If we have e.g. DatetimeTZDtype[us, UTC],
    #  then values.dtype should be M8[us].
    assert dtype._creso == get_unit_from_dtype(values.dtype)

result = super()._simple_new(values, dtype)
result._freq = freq
exit(result)
