# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# See gh-12912
data = "a b c~1 2 3~4 5 6~7 8 9"
parser = c_parser_only

df = parser.read_csv(StringIO(data), lineterminator="~", delim_whitespace=True)
expected = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["a", "b", "c"])
tm.assert_frame_equal(df, expected)
