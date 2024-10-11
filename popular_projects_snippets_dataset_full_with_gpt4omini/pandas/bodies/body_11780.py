# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
data = """index,A,B,C,D
foo,2,3,4,5
bar,7,8,9,10
baz,12,13,14,15
qux,12,13,14,15
foo2,12,13,14,15
bar2,12,13,14,15
"""
msg = r"'nrows' must be an integer >=0"
parser = all_parsers

with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), nrows=nrows)
