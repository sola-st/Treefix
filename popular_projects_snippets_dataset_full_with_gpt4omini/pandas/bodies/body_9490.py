# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_construction.py
# error in converting existing arrays to BooleanArray
msg = "Need to pass bool-like value"
with pytest.raises(TypeError, match=msg):
    pd.array(values, dtype="boolean")
