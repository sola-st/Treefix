# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
# GH15132: non-ascii unicode characters
# \u201d == RIGHT DOUBLE QUOTATION MARK

# simulate file handle
json = '{"a": "foo”", "b": "bar"}\n{"a": "foo", "b": "bar"}\n'
json = StringIO(json)
result = read_json(json, lines=True)
expected = DataFrame([["foo\u201d", "bar"], ["foo", "bar"]], columns=["a", "b"])
tm.assert_frame_equal(result, expected)

# simulate string
json = '{"a": "foo”", "b": "bar"}\n{"a": "foo", "b": "bar"}\n'
result = read_json(json, lines=True)
expected = DataFrame([["foo\u201d", "bar"], ["foo", "bar"]], columns=["a", "b"])
tm.assert_frame_equal(result, expected)
