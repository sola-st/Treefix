# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
df = DataFrame([["a"], ["a"], ["a"], ["b"], ["a"]], columns=["A"])
g = df.groupby("A")
sg = g.A

expected = Series([0, 1, 2, 0, 3])

tm.assert_series_equal(expected, g.cumcount())
tm.assert_series_equal(expected, sg.cumcount())
