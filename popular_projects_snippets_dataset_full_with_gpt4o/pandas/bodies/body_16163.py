# Extracted from ./data/repos/pandas/pandas/tests/series/test_iteration.py
for idx, val in datetime_series.items():
    assert val == datetime_series[idx]
