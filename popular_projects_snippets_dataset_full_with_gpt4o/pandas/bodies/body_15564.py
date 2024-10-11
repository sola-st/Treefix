# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
# GH 20869
result = Series(dtype="datetime64[ns, UTC]").reindex([0, 1])
expected = Series([NaT] * 2, dtype="datetime64[ns, UTC]")
tm.assert_equal(result, expected)
