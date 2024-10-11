# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
pi = PeriodIndex(["2000", "2001"], freq="D")
offset = offsets.Day(2)
assert pi._maybe_convert_timedelta(offset) == 2
assert pi._maybe_convert_timedelta(2) == 2

offset = offsets.BusinessDay()
msg = r"Input has different freq=B from PeriodIndex\(freq=D\)"
with pytest.raises(ValueError, match=msg):
    pi._maybe_convert_timedelta(offset)
