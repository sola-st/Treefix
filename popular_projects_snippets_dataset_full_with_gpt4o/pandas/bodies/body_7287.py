# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_astype.py
# GH 13149, GH 13209
idx = TimedeltaIndex([1e14, "NaT", NaT, np.NaN])
msg = "Cannot cast TimedeltaIndex to dtype"
with pytest.raises(TypeError, match=msg):
    idx.astype(dtype)
