# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
if "name" in kwargs and "names" in kwargs:
    raise TypeError("Can only provide one of `names` and `name`")
if "name" in kwargs:
    kwargs["names"] = kwargs.pop("name")

exit(meth(self_or_cls, *args, **kwargs))
