# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_logical.py
a = pd.array([True, False], dtype="boolean")
with pytest.raises(TypeError, match=str(type(other).__name__)):
    getattr(a, all_logical_operators)(other)
