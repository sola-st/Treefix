# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_first_valid_index.py
# GH#9752 Series/DataFrame should both return None, not raise
obj = frame_or_series([np.nan])

assert obj.first_valid_index() is None
assert obj.iloc[:0].first_valid_index() is None
