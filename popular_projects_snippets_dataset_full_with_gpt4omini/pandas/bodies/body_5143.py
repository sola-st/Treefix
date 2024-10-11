# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#18846
td = Timedelta(hours=3, minutes=3)
ser = pd.Series([1], dtype=np.int64)
res = td.__rfloordiv__(ser)
assert res is NotImplemented

msg = "Invalid dtype"
with pytest.raises(TypeError, match=msg):
    # Deprecated GH#19761, enforced GH#29797
    ser // td
