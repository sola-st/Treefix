# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py

name = maybe_extract_name(name, data, cls)

with rewrite_exception("IntervalArray", cls.__name__):
    array = IntervalArray(
        data,
        closed=closed,
        copy=copy,
        dtype=dtype,
        verify_integrity=verify_integrity,
    )

exit(cls._simple_new(array, name))
