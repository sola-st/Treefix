# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
# check that the result with non-nano matches nano
off = _create_offset(offset_types)

dti = date_range("2016-01-01", periods=35, freq="D")

arr = dti._data._ndarray.astype(f"M8[{unit}]")
dta = type(dti._data)._simple_new(arr, dtype=arr.dtype)

with warnings.catch_warnings(record=True) as w:
    expected = dti._data + off
    result = dta + off

exp_unit = unit
if isinstance(off, Tick) and off._creso > dta._creso:
    # cast to higher reso like we would with Timedelta scalar
    exp_unit = Timedelta(off).unit
expected = expected.as_unit(exp_unit)

if len(w):
    # PerformanceWarning was issued bc _apply_array raised, so we
    #  fell back to object dtype, for which the code path does
    #  not yet cast back to the original resolution
    mark = pytest.mark.xfail(
        reason="Goes through object dtype in DatetimeArray._add_offset, "
        "doesn't restore reso in result"
    )
    request.node.add_marker(mark)

tm.assert_numpy_array_equal(result._ndarray, expected._ndarray)
