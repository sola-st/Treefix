# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_dropna.py
for ser in [
    Series([1, 2, 3], name="x"),
    Series([False, True, False], name="x"),
]:

    result = ser.dropna()
    tm.assert_series_equal(result, ser)
    assert result is not ser

    s2 = ser.copy()
    return_value = s2.dropna(inplace=True)
    assert return_value is None
    tm.assert_series_equal(s2, ser)
