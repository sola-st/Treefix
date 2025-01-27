# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#39462
nat = np.datetime64("NaT", "ns")
arr = np.array([nat], dtype=object)
if frame_or_series is DataFrame:
    arr = arr.reshape(1, 1)

msg = "Invalid type for timedelta scalar: <class 'numpy.datetime64'>"
with pytest.raises(TypeError, match=msg):
    frame_or_series(arr, dtype="m8[ns]")
