# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
# GH#4226
tdi = timedelta_range("1d", "5d", freq="H", name="timebucket")
assert tdi[1:].name == tdi.name
