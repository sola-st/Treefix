# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
result = float_frame.apply(
    lambda x: list(range(len(float_frame.index))), result_type="broadcast"
)
m = list(range(len(float_frame.index)))
expected = DataFrame(
    {c: m for c in float_frame.columns},
    dtype="float64",
    index=float_frame.index,
)
tm.assert_frame_equal(result, expected)
