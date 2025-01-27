# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 18756
idx = IntervalIndex.from_tuples(tuples)
result = idx.to_tuples(na_tuple=na_tuple)

# check the non-NA portion
expected_notna = Index(com.asarray_tuplesafe(tuples[:-1]))
result_notna = result[:-1]
tm.assert_index_equal(result_notna, expected_notna)

# check the NA portion
result_na = result[-1]
if na_tuple:
    assert isinstance(result_na, tuple)
    assert len(result_na) == 2
    assert all(isna(x) for x in result_na)
else:
    assert isna(result_na)
