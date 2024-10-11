# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
# GH9180
result = read_json('{"a": 1, "b": 2}\n{"b":2, "a" :1}\n', lines=True)
expected = DataFrame([[1, 2], [1, 2]], columns=["a", "b"])
tm.assert_frame_equal(result, expected)
