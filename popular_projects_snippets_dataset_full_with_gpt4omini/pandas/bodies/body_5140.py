# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#18846
td = Timedelta(hours=3, minutes=3)

assert td.__rfloordiv__(np.nan) is NotImplemented
assert td.__rfloordiv__(3.5) is NotImplemented
assert td.__rfloordiv__(2) is NotImplemented
assert td.__rfloordiv__(np.float64(2.0)) is NotImplemented
assert td.__rfloordiv__(np.uint8(9)) is NotImplemented
assert td.__rfloordiv__(np.int32(2.0)) is NotImplemented

msg = r"unsupported operand type\(s\) for //: '.*' and 'Timedelta"
with pytest.raises(TypeError, match=msg):
    np.float64(2.0) // td
with pytest.raises(TypeError, match=msg):
    np.uint8(9) // td
with pytest.raises(TypeError, match=msg):
    # deprecated GH#19761, enforced GH#29797
    np.int32(2.0) // td
