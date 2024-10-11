# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_astype.py
obj = period_range("2000", periods=2, name="idx")
result = obj.astype("category")
expected = CategoricalIndex(
    [Period("2000-01-01", freq="D"), Period("2000-01-02", freq="D")], name="idx"
)
tm.assert_index_equal(result, expected)

result = obj._data.astype("category")
expected = expected.values
tm.assert_categorical_equal(result, expected)
