# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH 6410 / numpy 4328
# 32-bit under 1.9-dev indexing issue

df = DataFrame({"A": range(2), "B": [Timestamp("2000-01-1")] * 2})
result = df.groupby("A")["B"].transform(min)
expected = Series([Timestamp("2000-01-1")] * 2, name="B")
tm.assert_series_equal(result, expected)
