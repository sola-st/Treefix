# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py

# GH 4892
# float_indexers should raise exceptions
# on appropriate Index types & accessors

index = index_func(5)
s = gen_obj(frame_or_series, index)

# getitem
if indexer_sli is tm.iloc:
    msg = (
        "cannot do positional indexing "
        rf"on {type(index).__name__} with these indexers \[(3|4)\.0\] of "
        "type float"
    )
else:
    msg = (
        "cannot do slice indexing "
        rf"on {type(index).__name__} with these indexers "
        r"\[(3|4)(\.0)?\] "
        r"of type (float|int)"
    )
with pytest.raises(TypeError, match=msg):
    indexer_sli(s)[idx]

# setitem
if indexer_sli is tm.iloc:
    # otherwise we keep the same message as above
    msg = "slice indices must be integers or None or have an __index__ method"
with pytest.raises(TypeError, match=msg):
    indexer_sli(s)[idx] = 0
