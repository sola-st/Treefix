# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_to_timestamp.py
idx = period_range("2017", periods=12, freq="A-DEC")
result = idx.to_timestamp()
expected = date_range("2017", periods=12, freq="AS-JAN")
tm.assert_index_equal(result, expected)
