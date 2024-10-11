# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
obj = series_with_simple_index
if frame_or_series is not Series:
    obj = obj.to_frame()
exit(obj)
