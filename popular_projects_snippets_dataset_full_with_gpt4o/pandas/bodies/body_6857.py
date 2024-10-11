# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_base.py
# GH#30588 multi-dim indexing is deprecated, but raising is also acceptable
idx = simple_index
with pytest.raises(ValueError, match="multi-dimensional indexing not allowed"):
    idx[:, None]
with pytest.raises(ValueError, match="multi-dimensional indexing not allowed"):
    # GH#44051
    idx[True]
with pytest.raises(ValueError, match="multi-dimensional indexing not allowed"):
    # GH#44051
    idx[False]
