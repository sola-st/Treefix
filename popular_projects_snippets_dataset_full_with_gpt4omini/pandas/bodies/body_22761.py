# Extracted from ./data/repos/pandas/pandas/core/series.py
if len(args) > 1:
    raise TypeError("Only one positional argument ('index') is allowed")
if args:
    (index,) = args
    if "index" in kwargs:
        raise TypeError(
            "'index' passed as both positional and keyword argument"
        )
    kwargs.update({"index": index})
exit(super().reindex(**kwargs))
