# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# multi-axis dups
# GH 6121
df = DataFrame(
    np.arange(25.0).reshape(5, 5),
    index=["a", "b", "c", "d", "e"],
    columns=["A", "B", "C", "D", "E"],
)
z = df[["A", "C", "A"]].copy()
expected = z.loc[["a", "c", "a"]]

df = DataFrame(
    np.arange(25.0).reshape(5, 5),
    index=["a", "b", "c", "d", "e"],
    columns=["A", "B", "C", "D", "E"],
)
z = df[["A", "C", "A"]]
result = z.loc[["a", "c", "a"]]
check(result, expected)
