# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH15676
left = pd.DataFrame(
    [
        [to_datetime("20160602"), 1, "a"],
        [to_datetime("20160602"), 2, "a"],
        [to_datetime("20160603"), 1, "b"],
        [to_datetime("20160603"), 2, "b"],
    ],
    columns=["time", "k1", "k2"],
).set_index("time")

right = pd.DataFrame(
    [
        [to_datetime("20160502"), 1, "a", 1.0],
        [to_datetime("20160502"), 2, "a", 2.0],
        [to_datetime("20160503"), 1, "b", 3.0],
        [to_datetime("20160503"), 2, "b", 4.0],
    ],
    columns=["time", "k1", "k2", "value"],
).set_index("time")

expected = pd.DataFrame(
    [
        [to_datetime("20160602"), 1, "a", 1.0],
        [to_datetime("20160602"), 2, "a", 2.0],
        [to_datetime("20160603"), 1, "b", 3.0],
        [to_datetime("20160603"), 2, "b", 4.0],
    ],
    columns=["time", "k1", "k2", "value"],
).set_index("time")

result = merge_asof(
    left, right, left_index=True, right_index=True, by=["k1", "k2"]
)

tm.assert_frame_equal(expected, result)

with pytest.raises(
    MergeError, match="left_by and right_by must be same length"
):
    merge_asof(
        left,
        right,
        left_index=True,
        right_index=True,
        left_by=["k1", "k2"],
        right_by=["k1"],
    )
