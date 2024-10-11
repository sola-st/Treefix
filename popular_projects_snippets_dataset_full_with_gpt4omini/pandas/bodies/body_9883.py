# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
ser = Series([0.0, 0.1, 0.5, 0.9, 1.0])
msg = "quantile value -0.1 not in \\[0, 1\\]"
with pytest.raises(ValueError, match=msg):
    ser.rolling(3).quantile(-0.1)

msg = "quantile value 10.0 not in \\[0, 1\\]"
with pytest.raises(ValueError, match=msg):
    ser.rolling(3).quantile(10.0)

msg = "must be real number, not str"
with pytest.raises(TypeError, match=msg):
    ser.rolling(3).quantile("foo")
