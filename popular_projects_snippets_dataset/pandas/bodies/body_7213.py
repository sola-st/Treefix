# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_astype.py
# GH#13149
idx = Index([1, 2, non_finite], dtype=np.float64)

msg = r"Cannot convert non-finite values \(NA or inf\) to integer"
with pytest.raises(ValueError, match=msg):
    idx.astype(dtype)
