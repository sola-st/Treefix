# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
# slice with None at both ends, but not step

key = slice(None, None, "foo")

if isinstance(index, IntervalIndex):
    msg = "label-based slicing with step!=1 is not supported for IntervalIndex"
    with pytest.raises(ValueError, match=msg):
        index._convert_slice_indexer(key, "loc")
else:
    msg = "'>=' not supported between instances of 'str' and 'int'"
    with pytest.raises(TypeError, match=msg):
        index._convert_slice_indexer(key, "loc")
