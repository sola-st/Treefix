# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr = create_mgr("h: datetime-1; g: datetime-2")
assert mgr.as_array().dtype == "M8[ns]"
