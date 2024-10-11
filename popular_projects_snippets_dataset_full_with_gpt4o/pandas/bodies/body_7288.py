# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_astype.py
obj = timedelta_range("1H", periods=2, freq="H")

result = obj.astype("category")
expected = pd.CategoricalIndex([Timedelta("1H"), Timedelta("2H")])
tm.assert_index_equal(result, expected)

result = obj._data.astype("category")
expected = expected.values
tm.assert_categorical_equal(result, expected)
