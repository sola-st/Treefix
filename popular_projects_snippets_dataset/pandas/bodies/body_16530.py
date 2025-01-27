# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GH 15150
df = DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 6,
        "B": ["A", "B", "C"] * 8,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 4,
        "D": [0] * 24,
        "E": [0] * 24,
    }
)
result = crosstab(
    [df.A, df.B],
    df.C,
    values=df.D,
    aggfunc=np.sum,
    normalize=True,
    margins=True,
)
expected = DataFrame(
    np.array([0] * 29 + [1], dtype=float).reshape(10, 3),
    columns=Index(["bar", "foo", "All"], dtype="object", name="C"),
    index=MultiIndex.from_tuples(
        [
            ("one", "A"),
            ("one", "B"),
            ("one", "C"),
            ("three", "A"),
            ("three", "B"),
            ("three", "C"),
            ("two", "A"),
            ("two", "B"),
            ("two", "C"),
            ("All", ""),
        ],
        names=["A", "B"],
    ),
)
tm.assert_frame_equal(result, expected)
