# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 2810
ind = date_range(start="2000-01-01", freq="D", periods=10)
datetimes = [ts.to_pydatetime() for ts in ind]
dates = [ts.date() for ts in ind]
df = DataFrame(datetimes, columns=["datetimes"])
df["dates"] = dates
result = df.dtypes
expected = Series(
    [np.dtype("datetime64[ns]"), np.dtype("object")],
    index=["datetimes", "dates"],
)
tm.assert_series_equal(result, expected)
