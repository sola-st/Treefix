# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-21948
# As of 0.25.0, read_table is undeprecated
parser = all_parsers
data = "a\tb\n1\t2\n3\t4"
expected = parser.read_csv(StringIO(data), sep="\t")
result = parser.read_table(StringIO(data))
tm.assert_frame_equal(result, expected)
