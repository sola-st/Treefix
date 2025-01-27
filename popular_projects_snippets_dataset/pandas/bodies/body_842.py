# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr = create_mgr(mgr_string)
assert mgr.as_array().dtype == dtype
