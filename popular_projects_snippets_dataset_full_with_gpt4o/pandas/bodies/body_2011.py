# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-17007 and gh-17125
#
# For completeness.
ser = Series(["12345678901234567890", "1234567890", "ITEM"])

if isinstance(exp, str):
    with pytest.raises(ValueError, match=exp):
        to_numeric(ser, errors=errors)
else:
    result = to_numeric(ser, errors=errors)
    tm.assert_series_equal(result, ser)
