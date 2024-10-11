# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
s = Series([1, 2, 3])
with pytest.raises(ValueError, match="change the shape"):
    s.sort_index(key=lambda x: x[:1])
