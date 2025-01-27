# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19738
td = Timedelta(minutes=3)

result = op(td, 2)
assert result == Timedelta(minutes=6)

result = op(td, 1.5)
assert result == Timedelta(minutes=4, seconds=30)

assert op(td, np.nan) is NaT

assert op(-1, td).value == -1 * td.value
assert op(-1.0, td).value == -1.0 * td.value

msg = "unsupported operand type"
with pytest.raises(TypeError, match=msg):
    # timedelta * datetime is gibberish
    op(td, Timestamp(2016, 1, 2))

with pytest.raises(TypeError, match=msg):
    # invalid multiply with another timedelta
    op(td, td)
