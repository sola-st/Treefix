# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
df = DataFrame(
    {"A": [1, 1, 1, 3, 3, 3], "B": [1, 1, 1, 4, 4, 4], "C": [1, 1, 1, 3, 4, 4]}
)

result = df.groupby(["A", "B"]).aggregate(structure)
expected.index.names = ["A", "B"]
tm.assert_frame_equal(result, expected)
