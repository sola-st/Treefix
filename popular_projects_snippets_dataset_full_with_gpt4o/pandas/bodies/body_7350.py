# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
# GH#39462
nat = np.datetime64("NaT", "ns")
arr = np.array([nat], dtype=object)

msg = "Invalid type for timedelta scalar"
with pytest.raises(TypeError, match=msg):
    TimedeltaIndex(arr)

with pytest.raises(TypeError, match=msg):
    TimedeltaArray._from_sequence(arr)

with pytest.raises(TypeError, match=msg):
    sequence_to_td64ns(arr)

with pytest.raises(TypeError, match=msg):
    to_timedelta(arr)
