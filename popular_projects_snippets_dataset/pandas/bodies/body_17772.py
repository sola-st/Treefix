# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
# see gh-6407
msg = "cannot infer freq from a non-convertible dtype on a Series"
s = Series(np.arange(end))

with pytest.raises(TypeError, match=msg):
    frequencies.infer_freq(s)
