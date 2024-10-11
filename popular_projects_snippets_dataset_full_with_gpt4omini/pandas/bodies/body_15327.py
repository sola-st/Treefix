# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#30588 multi-dimensional indexing deprecated
with pytest.raises(ValueError, match="Multi-dimensional indexing"):
    datetime_series[:, np.newaxis]
