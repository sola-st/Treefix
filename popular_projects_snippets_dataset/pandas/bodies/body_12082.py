# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_comment.py
# see gh-4623
parser = all_parsers
data = "# notes\na,b,c\n# more notes\n1,2,3"

if header is None:
    expected = DataFrame({0: ["a", "1"], 1: ["b", "2"], 2: ["c", "3"]})
else:
    expected = DataFrame([[1, 2, 3]], columns=["a", "b", "c"])

result = parser.read_csv(StringIO(data), comment="#", header=header)
tm.assert_frame_equal(result, expected)
