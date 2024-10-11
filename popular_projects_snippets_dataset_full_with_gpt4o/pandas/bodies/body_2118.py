# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 29403
result = to_datetime(deque([Timestamp("2010-06-02 09:30:00")] * 51))
expected = to_datetime([Timestamp("2010-06-02 09:30:00")] * 51)
tm.assert_index_equal(result, expected)
