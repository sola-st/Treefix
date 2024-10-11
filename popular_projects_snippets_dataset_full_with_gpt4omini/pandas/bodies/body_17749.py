# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
index = DatetimeIndex(["12/31/1998", "1/3/1999"])
msg = "Need at least 3 dates to infer frequency"

with pytest.raises(ValueError, match=msg):
    frequencies.infer_freq(index)
