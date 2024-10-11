# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
first = Period(first)
last = Period(last)

exp_first = Period(exp_first, freq=freq)
exp_last = Period(exp_last, freq=freq)

freq = pd.tseries.frequencies.to_offset(freq)
result = _get_period_range_edges(first, last, freq)
expected = (exp_first, exp_last)
assert result == expected
