# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#41409
tz = tz_naive_fixture

dti = date_range("2016-01-01", periods=3, tz=tz)
dta = dti._data
dta[0] = NaT

obj = frame_or_series(dta)
result = obj.astype("string")

# Check that Series/DataFrame.astype matches DatetimeArray.astype
expected = frame_or_series(dta.astype("string"))
tm.assert_equal(result, expected)

item = result.iloc[0]
if frame_or_series is DataFrame:
    item = item.iloc[0]
assert item is pd.NA

# For non-NA values, we should match what we get for non-EA str
alt = obj.astype(str)
assert np.all(alt.iloc[1:] == result.iloc[1:])
