# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
# GH 49897
offset = DateOffset(**offset_kwargs)
ts = Timestamp("2022-01-01")
result = ts + offset
expected = Timestamp(expected_arg)

assert result == expected
