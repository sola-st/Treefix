# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_join.py
start, end = datetime(2009, 1, 1), datetime(2010, 1, 1)
naive = date_range(start, end, freq=BDay(), tz=None)
aware = date_range(start, end, freq=BDay(), tz="Asia/Hong_Kong")

msg = "tz-naive.*tz-aware"
with pytest.raises(TypeError, match=msg):
    naive.join(aware)

with pytest.raises(TypeError, match=msg):
    aware.join(naive)
