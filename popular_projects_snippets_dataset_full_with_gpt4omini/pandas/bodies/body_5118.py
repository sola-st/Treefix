# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta("1 day")
other = np.array([Timedelta("2 Days").to_timedelta64()])

msg = (
    "ufunc '?multiply'? cannot use operands with types "
    rf"dtype\('{tm.ENDIAN}m8\[ns\]'\) and dtype\('{tm.ENDIAN}m8\[ns\]'\)"
)
with pytest.raises(TypeError, match=msg):
    td * other
with pytest.raises(TypeError, match=msg):
    other * td
