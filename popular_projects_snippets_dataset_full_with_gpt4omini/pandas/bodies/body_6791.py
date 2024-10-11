# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH 20921
index = IntervalIndex.from_tuples([(0, 5)], closed=closed)
interval = Interval(left, right, closed=other_closed)
if interval == index[0]:
    result = index.get_loc(interval)
    assert result == 0
else:
    with pytest.raises(
        KeyError,
        match=re.escape(f"Interval({left}, {right}, closed='{other_closed}')"),
    ):
        index.get_loc(interval)
