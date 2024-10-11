# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
# GH#27358
expected = DataFrame([[{"a": 1, "b": 2}, {"a": 3, "b": 4}]]).T
data = Series([[{"a": 1, "b": 2}], [{"a": 3, "b": 4}]])
result = DataFrame.from_records(data)
tm.assert_frame_equal(result, expected)
