# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#4892
# float_indexers should raise exceptions
# on appropriate Index types & accessors
# this duplicates the code below
# but is specifically testing for the error
# message

obj = series_with_simple_index
if frame_or_series is DataFrame:
    obj = obj.to_frame()

msg = "Cannot index by location index with a non-integer key"
with pytest.raises(TypeError, match=msg):
    obj.iloc[3.0]

with pytest.raises(IndexError, match=_slice_iloc_msg):
    obj.iloc[3.0] = 0
