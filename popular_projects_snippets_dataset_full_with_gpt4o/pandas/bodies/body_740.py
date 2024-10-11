# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
assert not is_scalar(zerodim)
assert is_scalar(lib.item_from_zerodim(zerodim))
