# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_python_parser_only.py
# see gh-15925 (comment)
data = "a\n1\n2"
parser = python_parser_only
msg = "skipfooter cannot be negative"

with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), skipfooter=-1)
