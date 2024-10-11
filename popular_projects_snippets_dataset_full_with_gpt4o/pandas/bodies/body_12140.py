# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_python_parser_only.py
# see gh-13879 and gh-15910
parser = python_parser_only
if skipfooter:
    msg = "parsing errors in the skipped footer rows"
    with pytest.raises(ParserError, match=msg):
        parser.read_csv(StringIO(data), skipfooter=skipfooter)
else:
    msg = "unexpected end of data|expected after"
    with pytest.raises(ParserError, match=msg):
        parser.read_csv(StringIO(data), skipfooter=skipfooter)
