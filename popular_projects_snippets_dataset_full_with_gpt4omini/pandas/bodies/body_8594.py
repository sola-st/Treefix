# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
arr = ["1/1/2005", "1/2/2005", "Jn 3, 2005", "2005-01-04"]
msg = r"(\(')?Unknown datetime string format(:', 'Jn 3, 2005'\))?"
with pytest.raises(ValueError, match=msg):
    DatetimeIndex(arr)

arr = ["1/1/2005", "1/2/2005", "1/3/2005", "2005-01-04"]
idx1 = DatetimeIndex(arr)

arr = [datetime(2005, 1, 1), "1/2/2005", "1/3/2005", "2005-01-04"]
idx2 = DatetimeIndex(arr)

arr = [Timestamp(datetime(2005, 1, 1)), "1/2/2005", "1/3/2005", "2005-01-04"]
idx3 = DatetimeIndex(arr)

arr = np.array(["1/1/2005", "1/2/2005", "1/3/2005", "2005-01-04"], dtype="O")
idx4 = DatetimeIndex(arr)

idx5 = DatetimeIndex(["12/05/2007", "25/01/2008"], dayfirst=True)
idx6 = DatetimeIndex(
    ["2007/05/12", "2008/01/25"], dayfirst=False, yearfirst=True
)
tm.assert_index_equal(idx5, idx6)

for other in [idx2, idx3, idx4]:
    assert (idx1.values == other.values).all()

sdate = datetime(1999, 12, 25)
edate = datetime(2000, 1, 1)
idx = date_range(start=sdate, freq="1B", periods=20)
assert len(idx) == 20
assert idx[0] == sdate + 0 * offsets.BDay()
assert idx.freq == "B"

idx1 = date_range(start=sdate, end=edate, freq="W-SUN")
idx2 = date_range(start=sdate, end=edate, freq=offsets.Week(weekday=6))
assert len(idx1) == len(idx2)
assert idx1.freq == idx2.freq

idx1 = date_range(start=sdate, end=edate, freq="QS")
idx2 = date_range(
    start=sdate, end=edate, freq=offsets.QuarterBegin(startingMonth=1)
)
assert len(idx1) == len(idx2)
assert idx1.freq == idx2.freq

idx1 = date_range(start=sdate, end=edate, freq="BQ")
idx2 = date_range(
    start=sdate, end=edate, freq=offsets.BQuarterEnd(startingMonth=12)
)
assert len(idx1) == len(idx2)
assert idx1.freq == idx2.freq
