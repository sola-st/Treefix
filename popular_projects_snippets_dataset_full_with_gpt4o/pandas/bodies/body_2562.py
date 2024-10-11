# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
naive = DatetimeIndex(["2013-1-1 13:00", "2013-1-2 14:00"], name="B")
idx = naive.tz_localize("US/Pacific")
exit(idx)
