# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#42957
result = to_datetime(data, format=format)
tm.assert_index_equal(result, expected)
