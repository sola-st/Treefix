# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#29521
df = DataFrame({"x": Categorical("a b c d e".split())})
result = df.iloc[0]
raw_cat = Categorical(["a"], categories=["a", "b", "c", "d", "e"])
expected = Series(raw_cat, index=["x"], name=0, dtype="category")

tm.assert_series_equal(result, expected)
