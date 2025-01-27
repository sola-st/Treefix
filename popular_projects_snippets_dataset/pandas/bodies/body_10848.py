# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_quantile.py
# https://github.com/pandas-dev/pandas/issues/27526
df = DataFrame({"A": [0, 1, 2, 3, 4]})
key = np.array([0, 0, 1, 1, 1], dtype=np.int64)
result = df.groupby(key).quantile([0.25])

index = pd.MultiIndex.from_product([[0, 1], [0.25]])
expected = DataFrame({"A": [0.25, 2.50]}, index=index)
tm.assert_frame_equal(result, expected)

df = DataFrame({"A": [0, 1, 2, 3], "B": [4, 5, 6, 7]})
index = pd.MultiIndex.from_product([[0, 1], [0.25, 0.75]])

key = np.array([0, 0, 1, 1], dtype=np.int64)
result = df.groupby(key).quantile([0.25, 0.75])
expected = DataFrame(
    {"A": [0.25, 0.75, 2.25, 2.75], "B": [4.25, 4.75, 6.25, 6.75]}, index=index
)
tm.assert_frame_equal(result, expected)
