# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
# GH#20464
tdi = timedelta_range(0, periods=10)
with pytest.raises(KeyError, match=re.escape(repr(key))):
    tdi.get_loc(key)
