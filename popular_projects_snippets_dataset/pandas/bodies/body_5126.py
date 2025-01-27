# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#31869 None gets cast to NaT
td = Timedelta(10, unit="d")

result = NaT / td
assert np.isnan(result)

result = None / td
assert np.isnan(result)

result = np.timedelta64("NaT") / td
assert np.isnan(result)

msg = r"unsupported operand type\(s\) for /: 'numpy.datetime64' and 'Timedelta'"
with pytest.raises(TypeError, match=msg):
    np.datetime64("NaT") / td

msg = r"unsupported operand type\(s\) for /: 'float' and 'Timedelta'"
with pytest.raises(TypeError, match=msg):
    np.nan / td
