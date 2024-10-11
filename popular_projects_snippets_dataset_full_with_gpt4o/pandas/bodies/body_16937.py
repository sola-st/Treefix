# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
# https://github.com/pandas-dev/pandas/issues/35460
df = DataFrame(columns=["a"]).astype("datetime64[ns, UTC]")

# pd.NaT gets inferred as tz-naive, so append result is tz-naive
result = df._append({"a": pd.NaT}, ignore_index=True)
expected = DataFrame({"a": [pd.NaT]}).astype(object)
tm.assert_frame_equal(result, expected)

# also test with typed value to append
df = DataFrame(columns=["a"]).astype("datetime64[ns, UTC]")
other = Series({"a": pd.NaT}, dtype="datetime64[ns]")
result = df._append(other, ignore_index=True)
expected = DataFrame({"a": [pd.NaT]}).astype(object)
tm.assert_frame_equal(result, expected)

# mismatched tz
other = Series({"a": pd.NaT}, dtype="datetime64[ns, US/Pacific]")
result = df._append(other, ignore_index=True)
expected = DataFrame({"a": [pd.NaT]}).astype(object)
tm.assert_frame_equal(result, expected)
