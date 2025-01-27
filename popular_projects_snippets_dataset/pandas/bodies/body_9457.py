# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_constructors.py
# ensure that the public constructor cannot create an invalid instance
arr = np.array([0, 0, 1], dtype=np.int64) * 3600 * 10**9

msg = (
    "Inferred frequency None from passed values does not "
    "conform to passed frequency D"
)
with pytest.raises(ValueError, match=msg):
    TimedeltaArray(arr.view("timedelta64[ns]"), freq="D")
