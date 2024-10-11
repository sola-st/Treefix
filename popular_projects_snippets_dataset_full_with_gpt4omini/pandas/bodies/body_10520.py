# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
# GH 18473
df = DataFrame({"A": [str(x) for x in range(3)], "B": [str(x) for x in range(3)]})
grouped = df.groupby("A", as_index=False, sort=False)
result = grouped.agg({"B": lambda x: list(x)})
expected = DataFrame(
    {"A": [str(x) for x in range(3)], "B": [[str(x)] for x in range(3)]}
)
tm.assert_frame_equal(result, expected)
