# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isin.py
# GH#16394
df = DataFrame({"A": [1, 2, 3], "B": ["a", "b", "f"]})
df["C"] = list(zip(df["A"], df["B"]))
result = df["C"].isin([(1, "a")])
tm.assert_series_equal(result, Series([True, False, False], name="C"))
