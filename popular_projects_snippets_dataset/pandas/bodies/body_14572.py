# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
from pandas.plotting._matplotlib.converter import get_datevalue

assert get_datevalue(None, "D") is None
assert get_datevalue(1987, "A") == 1987
assert get_datevalue(Period(1987, "A"), "M") == Period("1987-12", "M").ordinal
assert get_datevalue("1/1/1987", "D") == Period("1987-1-1", "D").ordinal
