# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH 29772
lst = [
    [True, True, True, False],
    [True, False, np.nan, False],
    [True, True, np.nan, False],
    [True, True, np.nan, False],
]
df = DataFrame(
    data=lst,
    columns=MultiIndex.from_tuples([("A", 0), ("A", 1), ("B", 0), ("B", 1)]),
)

gb = df.groupby(level=1, axis=1)
result = gb.sum(numeric_only=False)
expected = DataFrame({0: [2.0, True, True, True], 1: [1, 0, 1, 1]})

tm.assert_frame_equal(result, expected)
