# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 42915
df = DataFrame(
    {"value": range(10), "idx1": [1] * 5 + [2] * 5, "idx2": [1, 2, 3, 4, 5] * 2}
).set_index(["idx1", "idx2"])
other = DataFrame({"value": range(5), "idx2": [1, 2, 3, 4, 5]}).set_index(
    "idx2"
)
result = getattr(df.groupby(level=0).rolling(2), f)(other)
expected_data = ([np.nan] + [expected_val] * 4) * 2
expected = DataFrame(
    expected_data,
    columns=["value"],
    index=MultiIndex.from_arrays(
        [
            [1] * 5 + [2] * 5,
            [1] * 5 + [2] * 5,
            list(range(1, 6)) * 2,
        ],
        names=["idx1", "idx1", "idx2"],
    ),
)
tm.assert_frame_equal(result, expected)
