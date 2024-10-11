# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH#30588, GH#31479
idx = simple_index
msg = "Multi-dimensional indexing"
with pytest.raises(ValueError, match=msg):
    idx[:, None]

if not isinstance(idx, RangeIndex):
    # GH#44051 RangeIndex already raised pre-2.0 with a different message
    with pytest.raises(ValueError, match=msg):
        idx[True]
    with pytest.raises(ValueError, match=msg):
        idx[False]
else:
    msg = "only integers, slices"
    with pytest.raises(IndexError, match=msg):
        idx[True]
    with pytest.raises(IndexError, match=msg):
        idx[False]
