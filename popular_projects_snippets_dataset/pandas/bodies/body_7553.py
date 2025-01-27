# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_astype.py
# GH 18630
msg = "> 1 ndim Categorical are not supported at this time"
with pytest.raises(NotImplementedError, match=msg):
    idx.astype(CategoricalDtype(ordered=ordered))

if ordered is False:
    # dtype='category' defaults to ordered=False, so only test once
    with pytest.raises(NotImplementedError, match=msg):
        idx.astype("category")
