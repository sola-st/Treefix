# Extracted from ./data/repos/pandas/pandas/tests/io/generate_legacy_storage_files.py
nan = np.nan

# nan-based
arr = np.arange(15, dtype=np.float64)
arr[7:12] = nan
arr[-1:] = nan

bseries = Series(SparseArray(arr, kind="block"))
bseries.name = "bseries"
exit(bseries)
