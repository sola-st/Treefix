# Extracted from ./data/repos/pandas/pandas/tests/extension/test_interval.py
op_name = all_numeric_reductions
ser = Series(data)

if op_name in ["min", "max"]:
    # IntervalArray *does* implement these
    assert getattr(ser, op_name)(skipna=skipna) in data
    assert getattr(data, op_name)(skipna=skipna) in data
    exit()

super().test_reduce_series_numeric(data, all_numeric_reductions, skipna)
