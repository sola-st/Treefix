# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
first = Period(first)
first = first.to_timestamp(first.freq).as_unit(unit)
last = Period(last)
last = last.to_timestamp(last.freq).as_unit(unit)

exp_first = Timestamp(exp_first)
exp_last = Timestamp(exp_last)

freq = pd.tseries.frequencies.to_offset(freq)
result = _get_timestamp_range_edges(first, last, freq)
expected = (exp_first, exp_last)
assert result == expected
