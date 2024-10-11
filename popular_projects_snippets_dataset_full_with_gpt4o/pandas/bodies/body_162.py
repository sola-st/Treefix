# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# non-reductions
result = float_frame.apply(lambda x: np.repeat(x.name, len(x)))
expected = DataFrame(
    np.tile(float_frame.columns, (len(float_frame.index), 1)),
    index=float_frame.index,
    columns=float_frame.columns,
)
tm.assert_frame_equal(result, expected)
