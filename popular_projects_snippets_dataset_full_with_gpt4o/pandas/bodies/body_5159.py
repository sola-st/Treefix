# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
td = Timedelta(minutes=3)
msg = "unsupported operand type"

with pytest.raises(TypeError, match=msg):
    divmod(Timestamp("2018-01-22"), td)

with pytest.raises(TypeError, match=msg):
    divmod(15, td)

with pytest.raises(TypeError, match=msg):
    divmod(16.0, td)

msg = "Invalid dtype int"
with pytest.raises(TypeError, match=msg):
    divmod(np.array([22, 24]), td)
