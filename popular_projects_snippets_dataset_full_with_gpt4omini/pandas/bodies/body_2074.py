# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 13486
result = to_datetime(dates, format=fmt)
expected = Index(expected_dates)
tm.assert_equal(result, expected)
