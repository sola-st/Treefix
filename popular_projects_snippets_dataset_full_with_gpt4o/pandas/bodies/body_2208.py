# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
data = ["01/01/2011 00:00:00", "01-02-2011 00:00:00", "2011-01-03T00:00:00"]
ser = Series(np.array(data))
msg = (
    r'^time data "01-02-2011 00:00:00" doesn\'t match format '
    r'"%m/%d/%Y %H:%M:%S", at position 1$'
)
with pytest.raises(ValueError, match=msg):
    to_datetime(ser, cache=cache)
