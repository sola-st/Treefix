# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_python_parser_only.py
parser = python_parser_only
data = """ignore
A,B,C
1,2,3 # comment
1,2,3,4,5
2,3,4
footer
"""
msg = "Expected 3 fields in line 4, saw 5"
with pytest.raises(ParserError, match=msg):
    parser.read_csv(StringIO(data), header=1, comment="#", skipfooter=1)
