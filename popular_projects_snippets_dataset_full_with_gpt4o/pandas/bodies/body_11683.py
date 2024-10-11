# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
# GH#22144
parser = all_parsers
data = "x,1\ny,2,5\nz,3\n"
with pytest.raises(ParserError, match="Expected 2 fields in line 2, saw 3"):
    parser.read_csv(StringIO(data), names=["a", "b"], header=None)
