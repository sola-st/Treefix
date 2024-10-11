# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# https://github.com/pandas-dev/pandas/issues/35858
date = pd.Timestamp("2000")
ser = Series(
    1,
    index=MultiIndex.from_tuples([("a", date)], names=["a", "b"]),
    name="c",
)
result = ser.loc[:, [date]]
tm.assert_series_equal(result, ser)
