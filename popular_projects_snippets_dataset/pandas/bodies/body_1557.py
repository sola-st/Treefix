# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH37750
key = 0 if (indexer is tm.iloc or len(obj) == 0) else obj.index[0]

with pytest.raises(IndexingError, match=_one_ellipsis_message):
    indexer(obj)[..., ...]

with pytest.raises(IndexingError, match=_one_ellipsis_message):
    indexer(obj)[..., [key], ...]

with pytest.raises(IndexingError, match=_one_ellipsis_message):
    indexer(obj)[..., ..., key]

# one_ellipsis_message takes precedence over "Too many indexers"
#  only when the first key is Ellipsis
with pytest.raises(IndexingError, match="Too many indexers"):
    indexer(obj)[key, ..., ...]
