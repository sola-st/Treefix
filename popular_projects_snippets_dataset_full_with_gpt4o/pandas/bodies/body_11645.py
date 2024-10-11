# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
# GH#42022
parser = all_parsers
data = """a,a\n1,1"""
result = parser.read_csv(StringIO(data), dtype=str)
expected = DataFrame({"a": ["1"], "a.1": ["1"]})
tm.assert_frame_equal(result, expected)
