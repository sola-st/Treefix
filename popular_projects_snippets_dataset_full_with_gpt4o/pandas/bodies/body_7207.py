# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_astype.py
# GH#45309 used to incorrectly return Index with int64 dtype
idx = Index([0.0, 5.0, 10.0, 15.0, 20.0], dtype=np.float64)
result = idx.astype("u8")
expected = Index([0, 5, 10, 15, 20], dtype=np.uint64)
tm.assert_index_equal(result, expected, exact=True)

idx_with_negatives = idx - 10
with pytest.raises(ValueError, match="losslessly"):
    idx_with_negatives.astype(np.uint64)
