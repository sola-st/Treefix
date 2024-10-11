# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# GH#47844
ser = Series(["1970-01-01", "1970-01-01", "1970-01-01"], dtype="datetime64[ns]")
df = ser.to_frame()

msg = "Casting to unit-less dtype 'datetime64' is not supported"
with pytest.raises(TypeError, match=msg):
    ser.astype(np.datetime64)
with pytest.raises(TypeError, match=msg):
    df.astype(np.datetime64)
with pytest.raises(TypeError, match=msg):
    ser.astype("datetime64")
with pytest.raises(TypeError, match=msg):
    df.astype("datetime64")
