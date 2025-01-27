# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# coerce to float
# GH#19223 until 2.0 used to coerce to float
dtype = f"m8[{unit}]"
arr = np.array([[1, 2, 3]], dtype=dtype)
df = DataFrame(arr)
ser = df.iloc[:, 0]
tdi = Index(ser)
tda = tdi._values

if unit in ["us", "ms", "s"]:
    assert (df.dtypes == dtype).all()
    result = df.astype(dtype)
else:
    # We get the nearest supported unit, i.e. "s"
    assert (df.dtypes == "m8[s]").all()

    msg = (
        rf"Cannot convert from timedelta64\[s\] to timedelta64\[{unit}\]. "
        "Supported resolutions are 's', 'ms', 'us', 'ns'"
    )
    with pytest.raises(ValueError, match=msg):
        df.astype(dtype)
    with pytest.raises(ValueError, match=msg):
        ser.astype(dtype)
    with pytest.raises(ValueError, match=msg):
        tdi.astype(dtype)
    with pytest.raises(ValueError, match=msg):
        tda.astype(dtype)

    exit()

result = df.astype(dtype)
# The conversion is a no-op, so we just get a copy
expected = df
tm.assert_frame_equal(result, expected)
