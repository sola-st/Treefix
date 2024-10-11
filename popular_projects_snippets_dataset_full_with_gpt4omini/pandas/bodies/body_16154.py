# Extracted from ./data/repos/pandas/pandas/tests/series/test_reductions.py
# GH#9442
ser = Series(pd.date_range("20130101", periods=100000, freq="H"))
ser[0] += pd.Timedelta("1s 1ms")

# mean
result = (ser - ser.min()).mean()
expected = pd.Timedelta((pd.TimedeltaIndex(ser - ser.min()).asi8 / len(ser)).sum())

# the computation is converted to float so
# might be some loss of precision
assert np.allclose(result.value / 1000, expected.value / 1000)

# sum
msg = "overflow in timedelta operation"
with pytest.raises(ValueError, match=msg):
    (ser - ser.min()).sum()

s1 = ser[0:10000]
with pytest.raises(ValueError, match=msg):
    (s1 - s1.min()).sum()
s2 = ser[0:1000]
(s2 - s2.min()).sum()
