# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
td = Timedelta(10, unit="d")

msg = "bad operand type for unary ~"
with pytest.raises(TypeError, match=msg):
    ~td

# check this matches pytimedelta and timedelta64
with pytest.raises(TypeError, match=msg):
    ~(td.to_pytimedelta())

umsg = "ufunc 'invert' not supported for the input types"
with pytest.raises(TypeError, match=umsg):
    ~(td.to_timedelta64())
