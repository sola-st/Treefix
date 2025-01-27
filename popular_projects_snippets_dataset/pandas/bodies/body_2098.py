# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
dt64 = np.datetime64(np.iinfo(np.int64).max, "D")

msg = "Out of bounds nanosecond timestamp"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    Timestamp(dt64)
with pytest.raises(OutOfBoundsDatetime, match=msg):
    to_datetime(dt64, errors="raise", cache=cache)

assert to_datetime(dt64, errors="coerce", cache=cache) is NaT
