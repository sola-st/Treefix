# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_ticks.py
offset = kls(3)
td = Timedelta(hours=2)

for other in [td, td.to_pytimedelta(), td.to_timedelta64()]:
    result = offset + other
    assert isinstance(result, Timedelta)
    assert result == expected

    result = other + offset
    assert isinstance(result, Timedelta)
    assert result == expected
