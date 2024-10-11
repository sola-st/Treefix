# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
# test_map_dictlike generally tests

index = PeriodIndex([2005, 2007, 2009], freq="A")
result = index.map(lambda x: x.ordinal)
exp = Index([x.ordinal for x in index])
tm.assert_index_equal(result, exp)
