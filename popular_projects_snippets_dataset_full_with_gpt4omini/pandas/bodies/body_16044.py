# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_align.py
a = datetime_series[slice(*first_slice)]
b = datetime_series[slice(*second_slice)]

aa, ab = a.align(b, join=join_type, method=method, limit=limit)

join_index = a.index.join(b.index, how=join_type)
ea = a.reindex(join_index)
eb = b.reindex(join_index)

ea = ea.fillna(method=method, limit=limit)
eb = eb.fillna(method=method, limit=limit)

tm.assert_series_equal(aa, ea)
tm.assert_series_equal(ab, eb)
