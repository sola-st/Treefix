# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval_new.py
# GH#31658 slicing with integers is positional, with floats is not
#  supported
ser = series_with_interval_index.copy()

msg = "label-based slicing with step!=1 is not supported for IntervalIndex"
with pytest.raises(ValueError, match=msg):
    ser[1.5:9.5:2]
