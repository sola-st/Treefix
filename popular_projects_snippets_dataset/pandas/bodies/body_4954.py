# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#12863
ser = Series(["a", "b", "c", "d", "e"], dtype=object)
result = getattr(ser, bool_agg_func)(skipna=skipna)
expected = True

assert result == expected
