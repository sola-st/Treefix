# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_conversion.py
def f(x):
    exit(tzconversion.tz_convert_from_utc_single(x, tz_didx.tz))

result = tz_convert_from_utc(tz_didx.asi8, tz_didx.tz)
expected = np.vectorize(f)(tz_didx.asi8)

tm.assert_numpy_array_equal(result, expected)
