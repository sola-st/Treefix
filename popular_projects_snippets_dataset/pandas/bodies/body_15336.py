# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#33404 do _not_ fall back to positional since ints are ambiguous
idx = Index(range(4)).astype(dtype)
dti = date_range("2000-01-03", periods=3)
mi = pd.MultiIndex.from_product([idx, dti])
ser = Series(range(len(mi))[::-1], index=mi)

key = box([5])
with pytest.raises(KeyError, match="5"):
    ser[key]
