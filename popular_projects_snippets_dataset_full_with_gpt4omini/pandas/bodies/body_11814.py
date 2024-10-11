# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# GH 47566
parser = all_parsers
columns = ["a", "b", "c"]
data = "1,2"
result = parser.read_csv(StringIO(data), header=None, names=columns)
expected = DataFrame({"a": [1], "b": [2], "c": [np.nan]})
tm.assert_frame_equal(result, expected)
