# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
msg = r"times must be datetime64\[ns\] dtype."
with pytest.raises(ValueError, match=msg):
    Series(range(5)).ewm(times=np.arange(5))
