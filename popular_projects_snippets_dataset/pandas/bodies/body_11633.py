# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
parser = all_parsers
data = """\
one,two
1,2.5
2,3.5
3,4.5
4,5.5"""

with pytest.raises(TypeError, match="data type [\"']foo[\"'] not understood"):
    parser.read_csv(StringIO(data), dtype={"one": "foo", 1: "int"})
