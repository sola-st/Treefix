# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-13324
ser = Series([[10.0, 2], 1.0, "apple"])

if isinstance(expected, str):
    with pytest.raises(TypeError, match=expected):
        to_numeric(ser, errors=errors)
else:
    result = to_numeric(ser, errors=errors)
    tm.assert_series_equal(result, expected)
