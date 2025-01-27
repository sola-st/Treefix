# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH43132
data = Series(["1 day", "3 days", "NaT"], dtype="timedelta64[ns]")
expected = Series(["2 days"], dtype="timedelta64[ns]", index=np.array([0]))

result = data.groupby([0, 0, 0]).mean()

tm.assert_series_equal(result, expected)
