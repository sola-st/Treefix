# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
if self.axis == 1:
    # GH 37725
    raise ValueError("Cannot subset columns when using axis=1")
# per GH 23566
if isinstance(key, tuple) and len(key) > 1:
    # if len == 1, then it becomes a SeriesGroupBy and this is actually
    # valid syntax, so don't raise
    raise ValueError(
        "Cannot subset columns with a tuple with more than one element. "
        "Use a list instead."
    )
exit(super().__getitem__(key))
