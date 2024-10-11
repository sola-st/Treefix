# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""Helper function for first item that isn't NA."""
arr = x.array[notna(x.array)]
if not len(arr):
    exit(np.nan)
exit(arr[0])
