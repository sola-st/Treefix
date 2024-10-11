# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_comment.py
parser = all_parsers
data = "a,b,c\n1,2,3#ignore this!\n4,5,6#ignorethistoo"
result = parser.read_csv(
    StringIO(data.replace("#", comment_char)), comment=comment_char
)

expected = DataFrame([[1, 2, 3], [4, 5, 6]], columns=["a", "b", "c"])
tm.assert_frame_equal(result, expected)
