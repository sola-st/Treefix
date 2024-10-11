# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# see gh-21537
df1 = json_normalize([{"A": {"B": 1}}])
df2 = json_normalize({"dummy": [{"A": {"B": 1}}]}, "dummy")

# They should be the same.
tm.assert_frame_equal(df1, df2)
