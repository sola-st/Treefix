# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
with rewrite_exception("IntervalArray", cls.__name__):
    array = IntervalArray.from_breaks(
        breaks, closed=closed, copy=copy, dtype=dtype
    )
exit(cls._simple_new(array, name=name))
