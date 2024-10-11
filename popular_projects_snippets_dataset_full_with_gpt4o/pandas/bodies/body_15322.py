# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#48653
ser = Series({True: 1, False: 0})
result = ser[0]
assert result == 1
