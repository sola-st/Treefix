# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
# GH 23236
result = DataFrame({"a": [0, 1], "b": [4, 5]})
result.iat[0, 0] = None
expected = DataFrame({"a": [None, 1], "b": [4, 5]})
tm.assert_frame_equal(result, expected)
