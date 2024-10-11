# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH-37506, GH-41967
ser = Series(data, dtype=dtype)
expected = expected_data[skipna][bool_agg_func == "all"]

result = getattr(ser, bool_agg_func)(skipna=skipna)
assert (result is pd.NA and expected is pd.NA) or result == expected
