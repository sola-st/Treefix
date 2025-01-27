# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
# GH#48812
cat = Categorical(Series([1, 2], dtype="Int64"))
ser = Series([4], dtype="Int64")
result = cat.add_categories(ser)
expected = Categorical(
    Series([1, 2], dtype="Int64"), categories=Series([1, 2, 4], dtype="Int64")
)
tm.assert_categorical_equal(result, expected)

cat = Categorical(Series(["a", "b", "a"], dtype=StringDtype()))
ser = Series(["d"], dtype=StringDtype())
result = cat.add_categories(ser)
expected = Categorical(
    Series(["a", "b", "a"], dtype=StringDtype()),
    categories=Series(["a", "b", "d"], dtype=StringDtype()),
)
tm.assert_categorical_equal(result, expected)
