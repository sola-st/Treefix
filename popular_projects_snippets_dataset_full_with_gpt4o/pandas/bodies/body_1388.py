# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
ser = Series([0, 1, 2], index=[0, 1, 0])
assert ser.iloc[2] == 2
