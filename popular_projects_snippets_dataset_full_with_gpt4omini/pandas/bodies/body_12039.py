# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# see gh-9205: test certain malformed input files that cause
# buffer overflows in tokenizer.c
msg = "Buffer overflow caught - possible malformed input file."
parser = c_parser_only

with pytest.raises(ParserError, match=msg):
    parser.read_csv(StringIO(malformed))
