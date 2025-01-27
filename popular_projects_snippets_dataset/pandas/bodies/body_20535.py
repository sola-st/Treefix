# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
with rewrite_exception("IntervalArray", cls.__name__):
    arr = IntervalArray.from_tuples(data, closed=closed, copy=copy, dtype=dtype)
exit(cls._simple_new(arr, name=name))
