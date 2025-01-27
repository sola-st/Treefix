# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_read_errors.py
# Too few columns.
data = """A,B,C,D,E,F
1,2,3,4,5,6
6,7,8,9,10,11,12
11,12,13,14,15,16
"""
parser = all_parsers
msg = "Expected 6 fields in line 3, saw 7"

with pytest.raises(ParserError, match=msg):
    parser.read_csv(StringIO(data))
