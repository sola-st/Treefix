# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
dta, dti = dta_dti

assert repr(dta) == repr(dti._data).replace("[ns", f"[{unit}")
