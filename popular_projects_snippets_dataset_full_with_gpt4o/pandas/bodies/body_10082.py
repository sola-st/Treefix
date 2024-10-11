# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
msg = "times must be the same length as the object."
with pytest.raises(ValueError, match=msg):
    Series(range(5)).ewm(times=np.arange(4).astype("datetime64[ns]"))
