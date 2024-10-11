# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
dtype = f"datetime64[{unit}]"
na = np.array(
    [
        ["2015-01-01", "2015-01-02", "2015-01-03"],
        ["2017-01-01", "2017-01-02", "2017-02-03"],
    ],
    dtype=dtype,
    order=order,
)
df = DataFrame(na)
expected = DataFrame(na.astype("M8[ns]"))
if unit in ["M", "D", "h", "m"]:
    with pytest.raises(TypeError, match="Cannot cast"):
        expected.astype(dtype)

    # instead the constructor casts to the closest supported reso, i.e. "s"
    expected = expected.astype("datetime64[s]")
else:
    expected = expected.astype(dtype=dtype)

tm.assert_frame_equal(df, expected)
