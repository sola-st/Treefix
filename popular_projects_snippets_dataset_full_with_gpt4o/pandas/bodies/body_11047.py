# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 20420
df = DataFrame(
    {"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 0], "C": [1, 1, 1, 2, 2]},
    index=range(5),
)
result = df.groupby("C").apply(lambda x: x.A.sort_index())
expected = Series(
    range(1, 6),
    index=MultiIndex.from_tuples(
        [(1, 0), (1, 1), (1, 2), (2, 3), (2, 4)], names=["C", None]
    ),
    name="A",
)
tm.assert_series_equal(result, expected)
