# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
arr = np.array([pd.NaT.value + 1], dtype="timedelta64[m]")

msg = (
    "Cannot convert -9223372036854775807 minutes to "
    r"timedelta64\[s\] without overflow"
)
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    to_timedelta(arr)

with pytest.raises(OutOfBoundsTimedelta, match=msg):
    TimedeltaIndex(arr)

with pytest.raises(OutOfBoundsTimedelta, match=msg):
    TimedeltaArray._from_sequence(arr)
