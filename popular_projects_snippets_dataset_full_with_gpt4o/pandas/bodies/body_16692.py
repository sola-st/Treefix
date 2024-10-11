# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# timedelta64 issues with join/merge
# GH 5695

d = DataFrame.from_dict(
    {"d": [datetime(2013, 11, 5, 5, 56)], "t": [timedelta(0, 22500)]}
)
df = DataFrame(columns=list("dt"))
df = concat([df, d], ignore_index=True)
result = concat([df, d], ignore_index=True)
expected = DataFrame(
    {
        "d": [datetime(2013, 11, 5, 5, 56), datetime(2013, 11, 5, 5, 56)],
        "t": [timedelta(0, 22500), timedelta(0, 22500)],
    }
)
if using_array_manager:
    # TODO(ArrayManager) decide on exact casting rules in concat
    expected = expected.astype(object)
tm.assert_frame_equal(result, expected)
