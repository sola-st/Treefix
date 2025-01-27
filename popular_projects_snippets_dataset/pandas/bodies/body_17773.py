# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
# see gh-6407
msg = "Unknown datetime string format"

with pytest.raises(ValueError, match=msg):
    frequencies.infer_freq(Series(["foo", "bar"]))
