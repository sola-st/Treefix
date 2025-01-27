# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_first_valid_index.py
# GH#12800
assert empty.last_valid_index() is None
assert empty.first_valid_index() is None
