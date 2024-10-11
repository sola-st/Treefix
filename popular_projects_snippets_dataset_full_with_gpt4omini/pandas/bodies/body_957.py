# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval.py
tpls = [(0, 1), (2, 3), (4, 5)]
if direction == "decreasing":
    tpls = tpls[::-1]

idx = IntervalIndex.from_tuples(tpls, closed=closed)
ser = Series(list("abc"), idx)

for key, expected in zip(idx.left, ser):
    if idx.closed_left:
        assert indexer_sl(ser)[key] == expected
    else:
        with pytest.raises(KeyError, match=str(key)):
            indexer_sl(ser)[key]

for key, expected in zip(idx.right, ser):
    if idx.closed_right:
        assert indexer_sl(ser)[key] == expected
    else:
        with pytest.raises(KeyError, match=str(key)):
            indexer_sl(ser)[key]

for key, expected in zip(idx.mid, ser):
    assert indexer_sl(ser)[key] == expected
