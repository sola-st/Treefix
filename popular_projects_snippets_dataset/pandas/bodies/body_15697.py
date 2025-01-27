# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_values.py
# GH41634
ser = Series([23, 7, 21])

msg = 'For argument "ascending" expected type bool, received type str.'
with pytest.raises(ValueError, match=msg):
    ser.sort_values(ascending="False")
