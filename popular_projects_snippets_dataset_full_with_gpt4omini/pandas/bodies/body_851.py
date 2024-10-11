# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
# will be converted according the actual dtype of the underlying
mgr = create_mgr("a: category")
assert mgr.as_array().dtype == "i8"
mgr = create_mgr("a: category; b: category2")
assert mgr.as_array().dtype == "object"
mgr = create_mgr("a: category2")
assert mgr.as_array().dtype == "object"

# combinations
mgr = create_mgr("a: f8")
assert mgr.as_array().dtype == "f8"
mgr = create_mgr("a: f8; b: i8")
assert mgr.as_array().dtype == "f8"
mgr = create_mgr("a: f4; b: i8")
assert mgr.as_array().dtype == "f8"
mgr = create_mgr("a: f4; b: i8; d: object")
assert mgr.as_array().dtype == "object"
mgr = create_mgr("a: bool; b: i8")
assert mgr.as_array().dtype == "object"
mgr = create_mgr("a: complex")
assert mgr.as_array().dtype == "complex"
mgr = create_mgr("a: f8; b: category")
assert mgr.as_array().dtype == "f8"
mgr = create_mgr("a: M8[ns]; b: category")
assert mgr.as_array().dtype == "object"
mgr = create_mgr("a: M8[ns]; b: bool")
assert mgr.as_array().dtype == "object"
mgr = create_mgr("a: M8[ns]; b: i8")
assert mgr.as_array().dtype == "object"
mgr = create_mgr("a: m8[ns]; b: bool")
assert mgr.as_array().dtype == "object"
mgr = create_mgr("a: m8[ns]; b: i8")
assert mgr.as_array().dtype == "object"
mgr = create_mgr("a: M8[ns]; b: m8[ns]")
assert mgr.as_array().dtype == "object"
