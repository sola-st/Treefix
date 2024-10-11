# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
# see gh-36895

left = DataFrame(
    data={
        "data": [1.5, 1.5],
    },
    index=MultiIndex.from_tuples(
        [[Timestamp("1950-01-01"), "A"], [Timestamp("1950-01-02"), "B"]],
        names=["date", "panel"],
    ),
)

right = DataFrame(
    index=MultiIndex.from_tuples([], names=["date", "panel"]), columns=["state"]
)

expected_index = MultiIndex.from_tuples(
    [[Timestamp("1950-01-01"), "A"], [Timestamp("1950-01-02"), "B"]],
    names=["date", "panel"],
)

if merge_type == "left":
    expected = DataFrame(
        data={
            "data": [1.5, 1.5],
            "state": [None, None],
        },
        index=expected_index,
    )
    results_merge = left.merge(right, how="left", on=["date", "panel"])
    results_join = left.join(right, how="left")
else:
    expected = DataFrame(
        data={
            "state": [None, None],
            "data": [1.5, 1.5],
        },
        index=expected_index,
    )
    results_merge = right.merge(left, how="right", on=["date", "panel"])
    results_join = right.join(left, how="right")

tm.assert_frame_equal(results_merge, expected)
tm.assert_frame_equal(results_join, expected)
