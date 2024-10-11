# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
# GH#25623 & GH 41130; enforced in 2.0
parser = all_parsers
data = """
a,b
1,2
    """
with pytest.raises(ParserError, match="Defining usecols without of bounds"):
    parser.read_csv(StringIO(data), usecols=[0, 2], names=names, header=0)
