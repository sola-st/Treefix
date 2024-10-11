# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_shift_diff.py
# GH 30134
now_dt = Timestamp.utcnow()
df = DataFrame({"a": [1, 1], "date": now_dt})
result = df.groupby("a").shift(0).iloc[0]
expected = Series({"date": now_dt}, name=result.name)
tm.assert_series_equal(result, expected)
