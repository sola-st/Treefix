# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 18756
idx = IntervalIndex.from_tuples(tuples)
result = idx.to_tuples()
expected = Index(com.asarray_tuplesafe(tuples))
tm.assert_index_equal(result, expected)
