# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
df = DataFrame({"A": [0] * 5})
g = df.groupby("A")
sg = g.A

expected = Series([0] * 5)

tm.assert_series_equal(expected, g.ngroup())
tm.assert_series_equal(expected, sg.ngroup())
