# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
obj = date_range("2000", periods=2, tz=tz, name="idx")
result = obj.astype("category")
expected = pd.CategoricalIndex(
    [Timestamp("2000-01-01", tz=tz), Timestamp("2000-01-02", tz=tz)],
    name="idx",
)
tm.assert_index_equal(result, expected)

result = obj._data.astype("category")
expected = expected.values
tm.assert_categorical_equal(result, expected)
