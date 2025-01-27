# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
df = DataFrame({"A": list("aaaba")})
g = df.groupby("A")
sg = g.A

expected = Series([0, 0, 0, 1, 0])

tm.assert_series_equal(expected, g.ngroup())
tm.assert_series_equal(expected, sg.ngroup())
