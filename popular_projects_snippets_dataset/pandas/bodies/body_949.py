# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval_new.py
# GH#31658 allows for integer step!=1, not Interval step
ser = series_with_interval_index.copy()
msg = "label-based slicing with step!=1 is not supported for IntervalIndex"
with pytest.raises(ValueError, match=msg):
    ser[0 : 4 : Interval(0, 1)]
