# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
idx = date_range("20130101", periods=4, freq="Q-NOV")
df = DataFrame(
    [[1, 1, 1, 5], [1, 1, 2, 5], [2, 1, 3, 5]], columns=["a", "a", "a", "a"]
)
df.columns = idx
expected = DataFrame([[1, 1, 1, 5], [1, 1, 2, 5], [2, 1, 3, 5]], columns=idx)
check(df, expected)
