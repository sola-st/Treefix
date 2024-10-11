# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_logical.py
op_name = all_logical_operators
a = pd.array([True, False, None], dtype="boolean")
msg = "Lengths must match"

with pytest.raises(ValueError, match=msg):
    getattr(a, op_name)([True, False])

with pytest.raises(ValueError, match=msg):
    getattr(a, op_name)(np.array([True, False]))

with pytest.raises(ValueError, match=msg):
    getattr(a, op_name)(pd.array([True, False], dtype="boolean"))
