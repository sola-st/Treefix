# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_period_asfreq.py
assert (
    period_asfreq(1, get_freq_code(freq1), get_freq_code(freq2), False) == expected
)
