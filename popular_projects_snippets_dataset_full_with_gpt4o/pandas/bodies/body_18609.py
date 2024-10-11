# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_period_asfreq.py
args = dt + (get_freq_code("W"),)
assert period_ordinal(*args) == expected
