# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
# In particular, check that datetime64 - Timestamp works GH#28286
td = Timedelta(1235345642000)
ts = Timestamp("2021-01-01", tz=tz_naive_fixture)
other = ts + td

assert other - ts == td
assert other.to_pydatetime() - ts == td
if tz_naive_fixture is None:
    assert other.to_datetime64() - ts == td
else:
    msg = "Cannot subtract tz-naive and tz-aware datetime-like objects"
    with pytest.raises(TypeError, match=msg):
        other.to_datetime64() - ts
