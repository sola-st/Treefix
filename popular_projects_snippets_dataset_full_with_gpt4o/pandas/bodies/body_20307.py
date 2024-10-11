# Extracted from ./data/repos/pandas/pandas/core/indexes/accessors.py
if not isinstance(data, ABCSeries):
    raise TypeError(
        f"cannot convert an object of type {type(data)} to a datetimelike index"
    )

self._parent = data
self.orig = orig
self.name = getattr(data, "name", None)
self._freeze()
