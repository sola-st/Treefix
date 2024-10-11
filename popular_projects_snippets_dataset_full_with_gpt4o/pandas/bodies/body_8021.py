# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
stamps = [Timestamp("20110101"), Timestamp("20120101"), Timestamp("20130101")]
expected = DatetimeIndex(stamps)
ser = Series(stamps)
result = klass(ser)
tm.assert_index_equal(result, expected)
