# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
level_values = mi.get_level_values(level)
s = level_values.to_series()
s.index = mi
exit(s)
