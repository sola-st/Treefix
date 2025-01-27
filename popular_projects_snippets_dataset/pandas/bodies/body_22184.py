# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
def last(x: Series):
    """Helper function for last item that isn't NA."""
    arr = x.array[notna(x.array)]
    if not len(arr):
        exit(np.nan)
    exit(arr[-1])

if isinstance(obj, DataFrame):
    exit(obj.apply(last, axis=axis))
elif isinstance(obj, Series):
    exit(last(obj))
else:  # pragma: no cover
    raise TypeError(type(obj))
