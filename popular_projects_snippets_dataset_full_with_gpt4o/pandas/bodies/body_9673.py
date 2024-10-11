# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_astype.py
arr = period_array(["2000", "2001", None], freq="D")
# slice off the [ns] so that the regex matches.
if other == "timedelta64[ns]":
    with pytest.raises(TypeError, match=other[:-4]):
        arr.astype(other)

else:
    # GH#45038 allow period->dt64 because we allow dt64->period
    result = arr.astype(other)
    expected = pd.DatetimeIndex(["2000", "2001", pd.NaT])._data
    tm.assert_datetime_array_equal(result, expected)
