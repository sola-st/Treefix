# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_searchsorted.py
idx = TimedeltaIndex(["1 day", "2 days", "3 days"])
msg = "value should be a 'Timedelta', 'NaT', or array of those. Got"
with pytest.raises(TypeError, match=msg):
    idx.searchsorted(arg)
