# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
# see gh-6407
#
# Cannot infer on PeriodIndex
msg = "cannot infer freq from a non-convertible dtype on a Series"
s = Series(period_range("2013", periods=10, freq=freq))

with pytest.raises(TypeError, match=msg):
    frequencies.infer_freq(s)
