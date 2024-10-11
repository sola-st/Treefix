# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_ticks.py
off = cls(10)
delta = off.delta
td64 = delta.to_timedelta64()
instance__type = ".".join([cls.__module__, cls.__name__])
msg = (
    "unsupported operand type\\(s\\) for \\/: 'int'|'float' and "
    f"'{instance__type}'"
)

with pytest.raises(TypeError, match=msg):
    2 / off
with pytest.raises(TypeError, match=msg):
    2.0 / off

assert (td64 * 2.5) / off == 2.5

if cls is not Nano:
    # skip pytimedelta for Nano since it gets dropped
    assert (delta.to_pytimedelta() * 2) / off == 2

result = np.array([2 * td64, td64]) / off
expected = np.array([2.0, 1.0])
tm.assert_numpy_array_equal(result, expected)
