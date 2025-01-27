# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py
# GH 13569
df = DataFrame({"a": [10, 20, 30]})
df["a"].loc[4] = 40
tm.assert_frame_equal(df, DataFrame({"a": [10, 20, 30]}))
tm.assert_series_equal(df["a"], Series([10, 20, 30], name="a"))
