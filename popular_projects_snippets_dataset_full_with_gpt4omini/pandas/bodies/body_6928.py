# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_indexing.py
with pytest.raises(ValueError, match="Invalid value for side kwarg"):
    Index([]).get_slice_bound("a", side="middle")
