# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
msg = "^Invalid argument/s or bad combination of arguments"
with pytest.raises(ValueError, match=msg):
    DateOffset(picoseconds=1)
