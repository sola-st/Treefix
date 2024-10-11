# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_array.py
# check we aren't on it
assert registry.find("decimal") is None
data = [decimal.Decimal("1"), decimal.Decimal("2")]

result = pd.array(data, dtype=DecimalDtype)
expected = DecimalArray._from_sequence(data)
tm.assert_equal(result, expected)
