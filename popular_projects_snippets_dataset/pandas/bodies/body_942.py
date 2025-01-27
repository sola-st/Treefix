# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
# GH#38053
s2 = Series((0, 1), index=[[False, True]])
result = s2.at[False]
assert result == 0
