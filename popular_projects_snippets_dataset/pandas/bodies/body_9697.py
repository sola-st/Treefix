# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
# GH#24623 check that invalid instances cannot be created with the
#  public constructor
arr = np.arange(5, dtype=np.int64) * 3600 * 10**9

msg = (
    "Inferred frequency H from passed values does not "
    "conform to passed frequency W-SUN"
)
with pytest.raises(ValueError, match=msg):
    DatetimeArray(arr, freq="W")
