# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
result = tm.round_trip_pickle(index)
tm.assert_index_equal(result, index, exact=True)
if result.nlevels > 1:
    # GH#8367 round-trip with timezone
    assert index.equal_levels(result)
