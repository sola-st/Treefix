# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#22492, GH#22508
dtimax = pd.to_datetime(["2021-12-28 17:19", Timestamp.max])
dtimin = pd.to_datetime(["2021-12-28 17:19", Timestamp.min])

ts_neg = pd.to_datetime(["1950-01-01", "1950-01-01"])
ts_pos = pd.to_datetime(["1980-01-01", "1980-01-01"])

# General tests
expected = Timestamp.max.value - ts_pos[1].value
result = dtimax - ts_pos
assert result[1].value == expected

expected = Timestamp.min.value - ts_neg[1].value
result = dtimin - ts_neg
assert result[1].value == expected
msg = "Overflow in int64 addition"
with pytest.raises(OverflowError, match=msg):
    dtimax - ts_neg

with pytest.raises(OverflowError, match=msg):
    dtimin - ts_pos

# Edge cases
tmin = pd.to_datetime([Timestamp.min])
t1 = tmin + Timedelta.max + Timedelta("1us")
with pytest.raises(OverflowError, match=msg):
    t1 - tmin

tmax = pd.to_datetime([Timestamp.max])
t2 = tmax + Timedelta.min - Timedelta("1us")
with pytest.raises(OverflowError, match=msg):
    tmax - t2
