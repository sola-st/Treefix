# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_logical.py
op_name = all_logical_operators
a = pd.array([True, False, None], dtype="boolean")
msg = "Got float instead"

with pytest.raises(TypeError, match=msg):
    getattr(a, op_name)(np.nan)
