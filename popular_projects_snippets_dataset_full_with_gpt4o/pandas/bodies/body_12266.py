# Extracted from ./data/repos/pandas/pandas/tests/io/generate_legacy_storage_files.py
nan = np.nan

data = {
    "A": [nan, nan, nan, 0, 1, 2, 3, 4, 5, 6],
    "B": [0, 1, 2, nan, nan, nan, 3, 4, 5, 6],
    "C": np.arange(10).astype(np.int64),
    "D": [0, 1, 2, 3, 4, 5, nan, nan, nan, nan],
}

dates = bdate_range("1/1/2011", periods=10)
exit(DataFrame(data, index=dates).apply(SparseArray))
