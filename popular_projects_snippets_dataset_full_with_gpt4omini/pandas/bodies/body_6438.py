# Extracted from ./data/repos/pandas/pandas/tests/extension/test_interval.py
msg = "can only insert Interval objects and NA into an IntervalArray"
with pytest.raises(TypeError, match=msg):
    data_missing.fillna([1, 1])
