# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#18846
td = Timedelta(hours=3, minutes=3)

dt64 = np.datetime64("2016-01-01", "us")

assert td.__rfloordiv__(dt64) is NotImplemented

msg = (
    r"unsupported operand type\(s\) for //: 'numpy.datetime64' and 'Timedelta'"
)
with pytest.raises(TypeError, match=msg):
    dt64 // td
