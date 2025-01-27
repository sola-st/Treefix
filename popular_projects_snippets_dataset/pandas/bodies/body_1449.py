# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_datetime.py
# GH#46903
ts = Timestamp("20130101").value
dti = pd.DatetimeIndex([ts + 50 + i for i in range(100)])
ser = Series(range(100), index=dti)

key = "2013-01-01 00:00:00.000000050+0000"
msg = re.escape(repr(key))
with pytest.raises(KeyError, match=msg):
    ser[key]

with pytest.raises(KeyError, match=msg):
    dti.get_loc(key)
