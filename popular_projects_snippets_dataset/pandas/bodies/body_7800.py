# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
# GH#35922. sort_values is stable both for normal and datetime-like Index
pidx = PeriodIndex(["2011", "2013", "2015", "2012", "2011"], name="pidx", freq="A")
iidx = Index([2011, 2013, 2015, 2012, 2011], name="idx")
ordered1, indexer1 = pidx.sort_values(return_indexer=True, ascending=False)
ordered2, indexer2 = iidx.sort_values(return_indexer=True, ascending=False)
tm.assert_numpy_array_equal(indexer1, indexer2)
