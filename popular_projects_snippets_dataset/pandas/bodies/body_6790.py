# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH 20921
index = IntervalIndex.from_tuples([(0, 5)], closed=closed)
if scalar in index[0]:
    result = index.get_loc(scalar)
    assert result == 0
else:
    with pytest.raises(KeyError, match=str(scalar)):
        index.get_loc(scalar)
