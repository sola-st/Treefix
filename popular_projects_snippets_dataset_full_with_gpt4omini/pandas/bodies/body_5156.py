# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
td = Timedelta(days=2, hours=6)

msg = r"unsupported operand type\(s\) for //: 'Timedelta' and 'Timestamp'"
with pytest.raises(TypeError, match=msg):
    divmod(td, Timestamp("2018-01-22"))
