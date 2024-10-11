# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# see GH21624
# this was crashing with "ValueError: Length of passed values is 1, index implies 0"
df = DataFrame({"g": [None], "x": 1})
actual = df.groupby("g")["x"].transform("sum")
expected = Series([np.nan], name="x")

tm.assert_series_equal(actual, expected)
