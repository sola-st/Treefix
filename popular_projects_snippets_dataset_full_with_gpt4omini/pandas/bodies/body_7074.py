# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
msg = "cannot sort an Index object in-place, use sort_values instead"
with pytest.raises(TypeError, match=msg):
    index.sort()
