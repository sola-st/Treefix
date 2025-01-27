# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py

exp_reso = max(ts._creso, Timedelta(td)._creso)

result = ts - td
expected = Timestamp(dt64) - td
assert isinstance(result, Timestamp)
assert result._creso == exp_reso
assert result == expected

result = ts + td
expected = Timestamp(dt64) + td
assert isinstance(result, Timestamp)
assert result._creso == exp_reso
assert result == expected

result = td + ts
expected = td + Timestamp(dt64)
assert isinstance(result, Timestamp)
assert result._creso == exp_reso
assert result == expected
