# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_shift_diff.py
# GH #24128
n_rows = 24
df = DataFrame(
    [(i % 12, i % 3, i) for i in range(n_rows)],
    dtype=float,
    columns=["A", "B", "Z"],
    index=None,
)
g = df.groupby(["A", "B"])

expected = DataFrame(
    [(i + 12 if i < n_rows - 12 else 0) for i in range(n_rows)],
    dtype=float,
    columns=["Z"],
    index=None,
)
result = g.shift(-1, fill_value=0)

tm.assert_frame_equal(result, expected)
