# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
result = json_normalize([])
expected = DataFrame()
tm.assert_frame_equal(result, expected)
