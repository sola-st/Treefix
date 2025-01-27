# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_iloc.py
# this is basically regular indexing
arr = np.random.randn(4, 3)
df = DataFrame(
    arr,
    columns=[["i", "i", "j"], ["A", "A", "B"]],
    index=[["i", "i", "j", "k"], ["X", "X", "Y", "Y"]],
)
result = df.iloc[2, 2]
expected = arr[2, 2]
assert result == expected
