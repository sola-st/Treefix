# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
if isinstance(obj, ABCDataFrame):
    exit(obj)
elif isinstance(obj, ABCSeries):
    if obj.name is None:
        raise ValueError("Cannot merge a Series without a name")
    exit(obj.to_frame())
else:
    raise TypeError(
        f"Can only merge Series or DataFrame objects, a {type(obj)} was passed"
    )
