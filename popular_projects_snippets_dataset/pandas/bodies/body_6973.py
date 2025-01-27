# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
dt_dates = [datetime(2012, 2, 9), datetime(2012, 2, 22)]

index1 = Index(dt_dates, dtype=object)
index2 = Index(["aa"], dtype=object)
result = index2.intersection(index1)

expected = Index([], dtype=object)
tm.assert_index_equal(result, expected)
