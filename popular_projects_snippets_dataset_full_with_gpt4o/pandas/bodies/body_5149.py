# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
td = Timedelta(hours=37)
msg = "unsupported operand type"
with pytest.raises(TypeError, match=msg):
    td % Timestamp("2018-01-22")

with pytest.raises(TypeError, match=msg):
    td % []
