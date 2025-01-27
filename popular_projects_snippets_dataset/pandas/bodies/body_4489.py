# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
dtype = f"timedelta64[{unit}]"
na = np.array(
    [
        [np.timedelta64(1, "D"), np.timedelta64(2, "D")],
        [np.timedelta64(4, "D"), np.timedelta64(5, "D")],
    ],
    dtype=dtype,
    order=order,
)
df = DataFrame(na)
if unit in ["D", "h", "m"]:
    # we get the nearest supported unit, i.e. "s"
    exp_unit = "s"
else:
    exp_unit = unit
exp_dtype = np.dtype(f"m8[{exp_unit}]")
expected = DataFrame(
    [
        [Timedelta(1, "D"), Timedelta(2, "D")],
        [Timedelta(4, "D"), Timedelta(5, "D")],
    ],
    dtype=exp_dtype,
)
# TODO(2.0): ideally we should get the same 'expected' without passing
#  dtype=exp_dtype.
tm.assert_frame_equal(df, expected)
