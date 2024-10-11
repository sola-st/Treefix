# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
obj = request.getfixturevalue(fixture)
assert nanops._bn_ok_dtype(obj.dtype, "test")
