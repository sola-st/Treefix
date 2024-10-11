# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_array.py
box = index_or_series

data = box([decimal.Decimal("1"), decimal.Decimal("2")])
# make sure it works
with pytest.raises(
    TypeError, match="scalars should not be of type pd.Series or pd.Index"
):
    DecimalArray2._from_sequence(data)

result = pd.array(data, dtype="decimal2")
expected = DecimalArray2._from_sequence(data.values)
tm.assert_equal(result, expected)
