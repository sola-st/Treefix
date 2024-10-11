# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-9710
parser = all_parsers
data = """\
MyColumn
a
b
a
b\n"""

expected = DataFrame({"MyColumn": list("abab")})
result = parser.read_csv(
    StringIO(data), skipinitialspace=True, delim_whitespace=delim_whitespace
)
tm.assert_frame_equal(result, expected)
