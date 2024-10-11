# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
with pytest.raises(ValueError, match="Multi-dimensional indexing"):
    series[:, None]
