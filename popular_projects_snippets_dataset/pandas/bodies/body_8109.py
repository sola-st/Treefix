# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH7774
dtype = any_real_numpy_dtype
index = Index(list("abc"))
labels = NumericIndex([], dtype=dtype)
assert index.reindex(labels)[0].dtype == dtype
