# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr = create_mgr("h: M8[ns, US/Eastern]; g: M8[ns, CET]")
assert mgr.iget(0).dtype == "datetime64[ns, US/Eastern]"
assert mgr.iget(1).dtype == "datetime64[ns, CET]"
assert mgr.as_array().dtype == "object"
