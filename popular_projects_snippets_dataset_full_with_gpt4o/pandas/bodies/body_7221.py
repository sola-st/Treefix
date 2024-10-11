# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
# GH#39382
idx = Index(vals)
with pytest.raises(KeyError, match="nan"):
    idx.get_loc(np.nan)
