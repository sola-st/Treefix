# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# see GH#19399
ser = Series({2**63 - 1: 3, 2**63: 4})
assert ser.loc[val] == expected
