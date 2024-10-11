# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# GH#37933
dtype = IntervalDtype(np.float64, "left")

msg = "dtype.closed and 'closed' do not match"
with pytest.raises(ValueError, match=msg):
    IntervalDtype(dtype, closed="both")
