# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
ser = Series([True, False, "apple"])

if isinstance(exp, str):
    with pytest.raises(ValueError, match=exp):
        to_numeric(ser, errors=errors)
else:
    result = to_numeric(ser, errors=errors)
    expected = Series(exp)

    tm.assert_series_equal(result, expected)
