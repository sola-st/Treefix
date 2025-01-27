# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#27709
ser = Series(data)
result = getattr(ser, bool_agg_func)(skipna=False)

# None is treated is False, but np.nan is treated as True
expected = bool_agg_func == "any" and None not in data
assert result == expected
