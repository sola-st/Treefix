# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
with pytest.raises(TypeError, match=f"unhashable type: '{type(index).__name__}'"):
    hash(index)
