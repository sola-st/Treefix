# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 25546
arg = "2019-01-01T00:00:00.000" + offset
result = to_datetime([arg], unit="ns", utc=utc)
expected = to_datetime([exp])
tm.assert_index_equal(result, expected)
