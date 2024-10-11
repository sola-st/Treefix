# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GH 50313
# use Float64 formats and function aggfunc with margins
df = DataFrame(
    {"A": [1, 2, 2, 1], "B": [3, 3, 4, 5], "C": [-1.0, 10.0, 1.0, 10.0]},
    dtype="Float64",
)
result = crosstab(
    df["A"],
    df["B"],
    values=df["C"],
    aggfunc="sum",
    margins=True,
)
expected = DataFrame(
    [
        [-1.0, pd.NA, 10.0, 9.0],
        [10.0, 1.0, pd.NA, 11.0],
        [9.0, 1.0, 10.0, 20.0],
    ],
    index=Index([1.0, 2.0, "All"], dtype="object", name="A"),
    columns=Index([3.0, 4.0, 5.0, "All"], dtype="object", name="B"),
    dtype="Float64",
)
tm.assert_frame_equal(result, expected)
