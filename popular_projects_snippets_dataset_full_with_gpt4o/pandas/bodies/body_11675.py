# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
# see gh-16338
msg = "header must be integer or list of integers"
data = """1,2\n3,4"""
parser = all_parsers

with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), header=header)
