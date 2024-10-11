# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 50342
df = DataFrame(
    {
        "A": ["foo", "foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar"],
        "B": ["one", "one", "one", "two", "two", "one", "one", "two", "two"],
        "C": [
            "small",
            "large",
            "large",
            "small",
            "small",
            "large",
            "small",
            "small",
            "large",
        ],
        "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
        "E": [2, 4, 5, 5, 6, 6, 8, 9, 9],
        ("col5",): [
            "foo",
            "foo",
            "foo",
            "foo",
            "foo",
            "bar",
            "bar",
            "bar",
            "bar",
        ],
        ("col6", 6): [
            "one",
            "one",
            "one",
            "two",
            "two",
            "one",
            "one",
            "two",
            "two",
        ],
        (7, "seven"): [
            "small",
            "large",
            "large",
            "small",
            "small",
            "large",
            "small",
            "small",
            "large",
        ],
    }
)
result = pivot_table(
    df, values="D", index=["A", "B"], columns=[(7, "seven")], aggfunc=np.sum
)
expected = DataFrame(
    [[4.0, 5.0], [7.0, 6.0], [4.0, 1.0], [np.nan, 6.0]],
    columns=Index(["large", "small"], name=(7, "seven")),
    index=MultiIndex.from_arrays(
        [["bar", "bar", "foo", "foo"], ["one", "two"] * 2], names=["A", "B"]
    ),
)
if using_array_manager:
    # INFO(ArrayManager) column without NaNs can preserve int dtype
    expected["small"] = expected["small"].astype("int64")
tm.assert_frame_equal(result, expected)
