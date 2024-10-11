# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
# Issue #18079
df = DataFrame(
    {"A": [1, 1, 1, 3, 3, 3], "B": [1, 1, 1, 4, 4, 4], "C": [1, 1, 1, 3, 4, 4]}
)

result = df.groupby("A")["C"].aggregate(structure)
expected.index.name = "A"
tm.assert_series_equal(result, expected)
