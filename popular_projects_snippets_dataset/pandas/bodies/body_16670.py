# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# #733, be a bit more 1337 about not returning unconsolidated DataFrame

left = DataFrame(
    {"key": [1, 1, 2, 2, 3], "value": list(range(5))}, columns=["value", "key"]
)
right = DataFrame({"key": [1, 1, 2, 3, 4, 5], "rvalue": list(range(6))})

joined = merge(left, right, on="key", how="outer")
expected = DataFrame(
    {
        "key": [1, 1, 1, 1, 2, 2, 3, 4, 5],
        "value": np.array([0, 0, 1, 1, 2, 3, 4, np.nan, np.nan]),
        "rvalue": [0, 1, 0, 1, 2, 2, 3, 4, 5],
    },
    columns=["value", "key", "rvalue"],
)
tm.assert_frame_equal(joined, expected)
