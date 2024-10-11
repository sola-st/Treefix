# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta(10, unit="d")
msg = "unsupported operand type"
for other in [2, 2.0, np.int64(2), np.float64(2)]:
    with pytest.raises(TypeError, match=msg):
        td + other
    with pytest.raises(TypeError, match=msg):
        other + td
    with pytest.raises(TypeError, match=msg):
        td - other
    with pytest.raises(TypeError, match=msg):
        other - td
