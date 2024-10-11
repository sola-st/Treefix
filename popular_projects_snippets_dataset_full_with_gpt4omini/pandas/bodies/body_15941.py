# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
ser = Series(range(10), index=[0, 3, 2, 1, 4, 5, 7, 6, 8, 9])
match = 'For argument "ascending" expected type bool'
with pytest.raises(ValueError, match=match):
    ser.sort_index(ascending=ascending)
