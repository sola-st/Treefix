# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_period_asfreq.py
# information for Jan. 1, 1970.
assert period_ordinal(1970, 1, 1, 0, 0, 0, 0, 0, get_freq_code(freq)) == expected
