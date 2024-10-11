# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 30667
df = DataFrame(
    [["x", "p"], ["x", "p"], ["x", "o"]], columns=["X", "Y"], index=[1, 2, 2]
)
if test_series:
    ser = df.set_index("Y")["X"]
    result = ser.groupby(level=0, group_keys=False).apply(lambda x: x)

    # not expecting the order to remain the same for duplicated axis
    result = result.sort_index()
    expected = ser.sort_index()
    tm.assert_series_equal(result, expected)
else:
    result = df.groupby("Y", group_keys=False).apply(lambda x: x)

    # not expecting the order to remain the same for duplicated axis
    result = result.sort_values("Y")
    expected = df.sort_values("Y")
    tm.assert_frame_equal(result, expected)
