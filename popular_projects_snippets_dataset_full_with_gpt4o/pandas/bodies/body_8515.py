# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH#20464
dti = date_range("1970-01-01", periods=10)
msg = "Cannot index DatetimeIndex with [Tt]imedelta"
with pytest.raises(TypeError, match=msg):
    dti.get_loc(key)
