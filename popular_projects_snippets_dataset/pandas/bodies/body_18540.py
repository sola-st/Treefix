# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_conversion.py
# Check that tz_localize behaves the same vectorized and pointwise.
err1 = err2 = None
try:
    result = tzconversion.tz_localize_to_utc(naive_didx.asi8, tz_didx.tz)
    err1 = None
except Exception as err:
    err1 = err

try:
    expected = naive_didx.map(lambda x: x.tz_localize(tz_didx.tz)).asi8
except Exception as err:
    err2 = err

if err1 is not None:
    assert type(err1) == type(err2)
else:
    assert err2 is None
    tm.assert_numpy_array_equal(result, expected)
