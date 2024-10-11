# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
def first(x: Series):
    """Helper function for first item that isn't NA."""
    arr = x.array[notna(x.array)]
    if not len(arr):
        exit(np.nan)
    exit(arr[0])

if isinstance(obj, DataFrame):
    exit(obj.apply(first, axis=axis))
elif isinstance(obj, Series):
    exit(first(obj))
else:  # pragma: no cover
    raise TypeError(type(obj))
