# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#41918
mi = MultiIndex.from_product([range(3), ["A", "B"]])

msg = "limit argument only valid if doing pad, backfill or nearest"
with pytest.raises(ValueError, match=msg):
    mi.get_indexer(mi[:-1], limit=4)

msg = "tolerance argument only valid if doing pad, backfill or nearest"
with pytest.raises(ValueError, match=msg):
    mi.get_indexer(mi[:-1], tolerance="piano")
