# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
a = Series(pd.array([1, 2], dtype="Int64"))
b = Series(to_decimal([1, 2]))

result = concat([a, b], ignore_index=True)
expected = Series([1, 2, Decimal(1), Decimal(2)], dtype=object)
tm.assert_series_equal(result, expected)
