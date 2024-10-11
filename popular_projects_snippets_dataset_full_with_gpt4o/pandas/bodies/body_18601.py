# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_np_datetime.py
# check that we raise, not segfault
arr = np.arange(5)
dtype = np.dtype("M8[ns]")

msg = (
    "astype_overflowsafe values.dtype and dtype must be either "
    "both-datetime64 or both-timedelta64"
)
with pytest.raises(TypeError, match=msg):
    astype_overflowsafe(arr, dtype, copy=True)

with pytest.raises(TypeError, match=msg):
    astype_overflowsafe(arr, dtype, copy=False)
