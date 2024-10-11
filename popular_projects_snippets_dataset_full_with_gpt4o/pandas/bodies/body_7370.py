# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_join.py
index = timedelta_range("1 day", periods=10)
joined = index.join(index, how=join_type)
tm.assert_index_equal(index, joined)
