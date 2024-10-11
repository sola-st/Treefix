# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
str(datetime_series)
# with Nones
ots = datetime_series.astype("O")
ots[::2] = None
repr(ots)
