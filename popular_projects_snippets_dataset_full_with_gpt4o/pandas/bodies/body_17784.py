# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_freq_code.py
msg = "Invalid frequency"

with pytest.raises(ValueError, match=msg):
    to_offset(str(args[0]) + args[1])
