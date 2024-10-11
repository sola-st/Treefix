# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH25170
# Test index=False in from_json to_json
expected = DataFrame({"a": [1, 2], "b": [3, 4]})
dfjson = expected.to_json(orient=orient, index=index)
result = read_json(dfjson, orient=orient)
tm.assert_frame_equal(result, expected)
