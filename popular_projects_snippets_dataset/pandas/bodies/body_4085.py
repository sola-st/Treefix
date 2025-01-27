# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# https://github.com/pandas-dev/pandas/issues/33256
arr = np.random.randint(1000, size=(10, 5))
df = DataFrame(arr, dtype="Int64")
result = df.mean(numeric_only=True)
expected = DataFrame(arr).mean()
tm.assert_series_equal(result, expected)
