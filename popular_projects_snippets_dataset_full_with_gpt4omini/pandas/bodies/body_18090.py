# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
rtol = 10**-decimals
s1 = Series([data1], dtype=dtype)
s2 = Series([data2], dtype=dtype)

if decimals in (5, 10) or (decimals >= 3 and abs(data1 - data2) >= 0.0005):
    msg = "Series values are different"
    with pytest.raises(AssertionError, match=msg):
        tm.assert_series_equal(s1, s2, rtol=rtol)
else:
    _assert_series_equal_both(s1, s2, rtol=rtol)
