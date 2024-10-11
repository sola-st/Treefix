# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
df = DataFrame({"A": list("abcde")})
g = df.groupby("A")
sg = g.A

expected = Series(range(5), dtype="int64")

tm.assert_series_equal(expected, g.ngroup())
tm.assert_series_equal(expected, sg.ngroup())
