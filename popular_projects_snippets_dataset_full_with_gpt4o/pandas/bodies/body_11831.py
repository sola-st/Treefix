# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_read_errors.py
# see gh-15925
parser = all_parsers
data = "a\n1\n1,2,3\n4\n5,6,7"

msg = "Expected 1 fields in line 3, saw 3"
with pytest.raises(ParserError, match=msg):
    parser.read_csv(StringIO(data), on_bad_lines="error")
