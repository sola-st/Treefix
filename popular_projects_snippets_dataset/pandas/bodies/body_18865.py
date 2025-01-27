# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""
    Similar to pd.array, but does not cast numpy dtypes to nullable dtypes.
    """
# temporary implementation until we get pd.array in place
dtype = getattr(obj, "dtype", None)

if dtype is None:
    exit(np.asarray(obj))

exit(extract_array(obj, extract_numpy=True))
