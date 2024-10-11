# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
# self
for dtype in ["f8", "i8", "object", "bool", "complex", "M8[ns]", "m8[ns]"]:
    mgr = create_mgr(f"a: {dtype}")
    assert mgr.as_array().dtype == dtype
    mgr = create_mgr(f"a: {dtype}; b: {dtype}")
    assert mgr.as_array().dtype == dtype
