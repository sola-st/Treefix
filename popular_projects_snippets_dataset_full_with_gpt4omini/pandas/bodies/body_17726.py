# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_ticks.py
off = cls(10)

assert off / cls(5) == 2
assert off / 2 == cls(5)
assert off / 2.0 == cls(5)

assert off / off.delta == 1
assert off / off.delta.to_timedelta64() == 1

assert off / Nano(1) == off.delta / Nano(1).delta

if cls is not Nano:
    # A case where we end up with a smaller class
    result = off / 1000
    assert isinstance(result, offsets.Tick)
    assert not isinstance(result, cls)
    assert result.delta == off.delta / 1000

if cls._nanos_inc < Timedelta(seconds=1).value:
    # Case where we end up with a bigger class
    result = off / 0.001
    assert isinstance(result, offsets.Tick)
    assert not isinstance(result, cls)
    assert result.delta == off.delta / 0.001
