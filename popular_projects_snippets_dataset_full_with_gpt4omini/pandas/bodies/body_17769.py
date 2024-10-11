# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
# see gh-10822
#
# Odd error message on conversions to datetime for unicode.
msg = "Unknown datetime string format"

with pytest.raises(ValueError, match=msg):
    frequencies.infer_freq(tm.makeStringIndex(10))
