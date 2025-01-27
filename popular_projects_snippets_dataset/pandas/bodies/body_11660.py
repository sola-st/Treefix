# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
# see gh-6114
parser = all_parsers
data = """\
MyColumn
a
b
a
b"""
msg = "Passing a bool to header is invalid"
with pytest.raises(TypeError, match=msg):
    parser.read_csv(StringIO(data), header=header)
