# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
if kwargs.get("freq") is not None:
    from pandas.core.resample import TimeGrouper

    cls = TimeGrouper
exit(super().__new__(cls))
