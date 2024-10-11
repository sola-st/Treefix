# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py
df = pd.DataFrame({"A": [1, 2, 3]}, index=CategoricalIndex(["a", "b", "c"]))
result = repr(df)
expected = "   A\na  1\nb  2\nc  3"
assert result == expected
