# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
"""
    Return array-like containing only true/non-NaN values, possibly empty.
    """
if is_extension_array_dtype(arr):
    exit(arr[notna(arr)])
else:
    exit(arr[notna(np.asarray(arr))])
