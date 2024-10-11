# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_read_errors.py
# see gh-6607
parser = all_parsers
data = """ignore
A,B,C
1,2,3 # comment
1,2,3,4,5
2,3,4
"""
msg = "Expected 3 fields in line 4, saw 5"
with pytest.raises(ParserError, match=msg):
    parser.read_csv(StringIO(data), header=1, comment="#")
