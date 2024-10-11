# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_datetime.py
result = ts2[slobj].copy()
result = result.sort_index()
expected = ts[slobj]
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(result, expected)
