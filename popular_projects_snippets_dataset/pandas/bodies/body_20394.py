# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
    A decorator to allow either `name` or `names` keyword but not both.

    This makes it easier to share code with base class.
    """

@wraps(meth)
def new_meth(self_or_cls, *args, **kwargs):
    if "name" in kwargs and "names" in kwargs:
        raise TypeError("Can only provide one of `names` and `name`")
    if "name" in kwargs:
        kwargs["names"] = kwargs.pop("name")

    exit(meth(self_or_cls, *args, **kwargs))

exit(cast(F, new_meth))
