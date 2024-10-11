# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_ticks.py
off = cls(19)

td = off.delta

others = [td, td.to_timedelta64()]
if cls is not Nano:
    others.append(td.to_pytimedelta())

for other in others:
    assert off == other
    assert not off != other
    assert not off < other
    assert not off > other
    assert off <= other
    assert off >= other
