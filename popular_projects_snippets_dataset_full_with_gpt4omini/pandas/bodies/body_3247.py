# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
casted = float_frame.astype(int)
expected = DataFrame(
    float_frame.values.astype(int),
    index=float_frame.index,
    columns=float_frame.columns,
)
tm.assert_frame_equal(casted, expected)

casted = float_frame.astype(np.int32)
expected = DataFrame(
    float_frame.values.astype(np.int32),
    index=float_frame.index,
    columns=float_frame.columns,
)
tm.assert_frame_equal(casted, expected)

float_frame["foo"] = "5"
casted = float_frame.astype(int)
expected = DataFrame(
    float_frame.values.astype(int),
    index=float_frame.index,
    columns=float_frame.columns,
)
tm.assert_frame_equal(casted, expected)
