# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
date_index = tm.makeDateIndex(24, freq="h", name="hourly")
expected = Index(range(24), dtype="int32", name="hourly")
tm.assert_index_equal(expected, date_index.map(lambda x: x.hour), exact=True)
